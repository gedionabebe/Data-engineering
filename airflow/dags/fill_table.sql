COPY traffic(track_id, v_type, traveled_d, avg_speed, lat, lon, speed, lon_acc, lat_acc, d_time)
FROM '../data/20181101_d10_1000_1030.csv'
DELIMITER ';'
CSV HEADER;