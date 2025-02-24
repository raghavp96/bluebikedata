echo "Building and pushing latest images to GKE Container Registry...\n"

PROJECT_ID="$(gcloud config get-value project -q)"

ROOT_DIR="../../"

for obj in $(less $ROOT_DIR/config.json | jq -c '.Network.Containers[]') 
do 
    ImgName="$(echo $obj | jq -r '.ImageName')"
    FolderName="$(echo $obj | jq -r '.Folder')"
    echo "Building image: ${ImgName}"
    echo "Image Folder: ${FolderName}"
    echo ""

    docker build -t gcr.io/${PROJECT_ID}/${ImgName}:v1 "$ROOT_DIR/$FolderName"

    echo "Pushing image to Google Container Registry: ${ImgName}"
    echo ""

    docker push gcr.io/${PROJECT_ID}/${ImgName}:v1

    echo "Done"
    sleep 5
done