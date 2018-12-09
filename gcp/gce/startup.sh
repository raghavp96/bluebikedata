# Talk to the metadata server to get the project id
PROJECTID=$(curl -s "http://metadata.google.internal/computeMetadata/v1/project/project-id" -H "Metadata-Flavor: Google")

# # Install logging monitor. The monitor will automatically pickup logs sent to
# # syslog.
# curl -s "https://storage.googleapis.com/signals-agents/logging/google-fluentd-install.sh" | bash
# service google-fluentd restart &

# Install dependencies from apt
apt-get update
apt-get install -yq \
    git build-essential supervisor python python-dev python-pip libffi-dev \
    libssl-dev

# # FROM https://cloud.google.com/python/tutorials/bookshelf-on-compute-engine#multiple_instances

# Create a pythonapp user. The application will run as this user.
useradd -m -d /home/pythonapp pythonapp

# pip from apt is out of date, so make it update itself and install virtualenv.
pip install --upgrade pip virtualenv

# Get the source code from the Google Cloud Repository
# git requires $HOME and it's not set during the startup script.
export HOME=/root
git config --global credential.helper gcloud.sh
git clone https://source.developers.google.com/p/cs3200-215502/r/bluebikedata /opt/app

# Make sure the pythonapp user owns the application code
chown -R pythonapp:pythonapp /opt/app

cd /opt/app
make start