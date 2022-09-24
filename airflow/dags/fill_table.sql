COPY traffic(id,track_id, v_type, traveled_d, avg_speed, lat, lon, speed, lon_acc, lat_acc, d_time)
FROM '/mnt/c/users/user/desktop/data-engineering/airflow/data/traffic_data.csv'
DELIMITER ','
CSV HEADER;