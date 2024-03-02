import json

def log(ID=None, TIME=None, DATA=None, WING_FL_POS=None, WING_FR_POS=None, WING_RL_POS=None, WING_RR_POS=None):
    file_path = "log.json"
    log_entry = {
        'ID': ID,
        'TIME': TIME,
        'DATA': DATA,
        'WING_FL_POS': WING_FL_POS,
        'WING_FR_POS': WING_FR_POS,
        'WING_RL_POS': WING_RL_POS,
        'WING_RR_POS': WING_RR_POS
    }

    try:
        with open(file_path, "a") as json_file:
            json.dump(log_entry, json_file)
            json_file.write('\n')
    except Exception as e:
        print("Error occurred:", e)

def main():
    log(1, "12:00", "Some data", 10, 20, 30, 40)

if __name__ == '__main__':
    main()