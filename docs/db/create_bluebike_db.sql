drop database if exists bluebike;

create database bluebike;

use bluebike;

create table if not exists station (
	station_id int primary key not null,
    station_name varchar(50) not null,
    latitude decimal(24,20) not null, -- Allows for up to 20 digits to the right of the decimal point, 24 digits altogether
    longitude decimal(24,20) not null,
    short_name varchar(50) not null,
    rental_methods enum('CREDITCARD', 'KEY', 'BOTH') not null,
    capacity int not null,
    rental_id varchar(100) not null,
    eightd_has_key_dispenser tinyint(2) not null,
    has_kiosk tinyint(2) not null
);

create table if not exists trip (
	trip_id int primary key not null,
    bike_id int not null,
    start_time datetime not null,
    end_time datetime not null,
    usertype enum('Customer', 'Subscriber') not null,
    birthyear year not null,
    gender tinyint not null,
    start_station int not null,
    stop_station int not null,
    foreign key (start_station) references station(station_id),
    foreign key (stop_station) references station(station_id)
);

create table if not exists station_status (
	station_status_id int not null,
    station_id int not null,
    num_bikes_available int not null,
    num_ebikes_available int not null,
    num_bikes_disabled int not null,
    num_docks_available int not null,
    num_dock_disabled int not null,
    is_installed tinyint not null,
    is_rented tinyint not null,
    is_returning tinyint not null,
    last_reported datetime not null,
    eightd_has_available_keys tinyint not null,
    primary key (station_status_id, station_id),
    foreign key (station_id) references station(station_id)    
);

-- Error Code: 1068. Multiple primary key defined

