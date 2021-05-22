import time
import csv

fitness_file = open("fitness.tcx", "r")

f = fitness_file.readlines()
fitness_table = open("fitness_table.csv","w")

fnames = ["time_str",
    "lat_str",
    "lon_str",
    "alt_str",
    "dist_str",
    "hr_str"]

writer = csv.DictWriter(fitness_table, fieldnames=fnames)
writer.writeheader()

time_list = []
latitude_list = []
longitude_list = []
altitude_delta = []
hr_List = []

for i, line in enumerate(f):
    line = line.strip()
    if line.startswith('<Id>'):
        session_id = str(line[4:14]+" "+line[15:26])
        print(session_id)

        date_time = time.strptime(str(line[4:14]+" "+line[15:22]), '%Y-%m-%d %H:%M:%S')
        #time = time.strptime(str(line[15:22]), '%H:%M:%S')
        print("date_time_object:", date_time)
        print ("Activity ID:", line)

    if line == "<Trackpoint>":
        #print("i=", i, "line=", line)
        #print(f[i+1])
        temp_str_dict = dict(
            time_str = f[i+1].strip(),
            lat_str = f[i+3].strip(),
            lon_str = f[i+4].strip(),
            alt_str = f[i+6].strip(),
            dist_str = f[i+7].strip(),
            hr_str = f[i+9].strip(),
        )
        print("temp_str_dict:", temp_str_dict)
        for key in temp_str_dict:
            start = temp_str_dict[key].find(">")+len(">")
            end = temp_str_dict[key].find("</")

            if key =="time_str":
                date_time_str = str(temp_str_dict[key][start:end])
                print("date_time_str", date_time_str)
                date_time = time.strptime(str(date_time_str[0:9]+" "+date_time_str[11:19]), '%Y-%m-%d %H:%M:%S')
                print("date/time object", date_time)
                temp_str_dict[key] = date_time_str
            else:
                temp_str_dict[key] = float(temp_str_dict[key][start:end])

        writer.writerow(temp_str_dict)
        print("temp_str_dict:", temp_str_dict)

        """
        print(f"time: {time_str}\n"
        f"latitude: {lat_str}\n"
        f"longitude: {lon_str}\n"
        f"altitude: {alt_str}\n"
        f"distance: {dist_str}\n"
        f"heart rate: {hr_str}\n")
        """
        

#distance_travelled = sqrt(int(alt_str)**2+int(alt_str)**2)

fitness_file.close()
fitness_table.close()

#<Id>2020-06-29T18:47:35.000+10:00</Id>
    


