import json
import os
import argparse
from pathlib import Path
from datetime import datetime
import time
import sys
sys.path.append('/home/serverpc/.local/lib/python3.8/site-packages')


if __name__ == "__main__":

## 최종 테스트용 user input ##

    correct_answer_1 = [
        {"Action json Sequence": [{"robot": "Deli-Buddy"},{"skill": "MoveTo", "location": 8109},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray1"},{"skill": "MoveTo", "location": 8111},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray8"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "Detect", "direction": "right"},{"skill": "MoveRobotArm", "item": "tray9"},{"skill": "MoveTo", "location": 8205},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray6"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8323},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray2"},{"skill": "MoveTo", "location": 8304},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray3"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8101},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray5"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot3"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8333},{"skill": "CleanUp"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8200}]},
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        {"Action json Sequence": [{"robot":"Robot3"},{"skill":"MoveTo","location":8222},{"skill":"CleanUp"},{"skill":"MoveTo","location":8200}]},
        ''
    ]
    correct_answer_2 = [
        {"Action json Sequence": [{"robot": "Deli-Buddy"},{"skill": "MoveTo", "location": 8109},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray1"},{"skill": "MoveTo", "location": 8111},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray8"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "Detect", "direction": "right"},{"skill": "MoveRobotArm", "item": "tray9"},{"skill": "MoveTo", "location": 8205},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray6"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8323},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray2"},{"skill": "MoveTo", "location": 8304},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray3"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8101},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray5"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot3"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8333},{"skill": "CleanUp"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8200}]},
        '',
        '',
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "VoiceOutput", "messages": "You have arrived at 8222."},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "VoiceOutput", "messages": "You have arrived at 8222."},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        '',
        '',
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "VoiceOutput", "messages": "I will take a picture in 5 seconds."},{"skill": "TakePicture"},{"skill": "SendPicture", "address": "010-1234-5678"},{"skill": "VoiceOutput", "messages": "Transmission is complete."}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8324},{"skill": "VoiceOutput", "messages": "You have arrived at room 8324."},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot5"},{"skill": "StartCollabot"},{"skill": "OpenDrawer", "book": "Harry Potter"},{"skill": "ExecuteDrawerDetector"},{"skill": "CloseDrawer"},{"skill": "Reset"}]},
        {"Action json Sequence": [{"robot": "Robot4"},{"skill": "DriveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "DriveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "DriveTo", "location": 8222},{"skill": "Spray"},{"skill": "DriveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "DriveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "DriveTo", "location": 8100}]},
        ''
    ]
    correct_answer_3 = [
        {"Action json Sequence": [{"robot": "Deli-Buddy"},{"skill": "MoveTo", "location": 8109},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray1"},{"skill": "MoveTo", "location": 8111},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray8"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "Detect", "direction": "right"},{"skill": "MoveRobotArm", "item": "tray9"},{"skill": "MoveTo", "location": 8205},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray6"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8323},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray2"},{"skill": "MoveTo", "location": 8304},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray3"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8101},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray5"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot3"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8333},{"skill": "CleanUp"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8200}]},
        {"Action json Sequence": [{"robot": "Robot9"},{"skill": "GoTo", "object": "Fork"},{"skill": "Pickup", "object": "Fork"},{"skill": "GoTo", "object": "Sink"},{"skill": "Put", "object": "Fork"},{"skill": "Switchon", "object": "Faucet"},{"skill": "Wash", "object": "Fork"},{"skill": "Switchoff", "object": "Faucet"},{"skill": "Pickup", "object": "Fork"},{"skill": "GoTo", "object": "Bowl"},{"skill": "Put", "object": "Fork"},{"skill": "ReturnHome"}]},        
        {"Action json Sequence": [{"robot": "Robot8"},{"skill": "GoTo", "object": "laptop"},{"skill": "Pickup", "object": "laptop"},{"skill": "GoTo", "object": "bed"},{"skill": "Put", "object": "laptop"},{"skill": "ReturnHome"}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "VoiceOutput", "messages": "You have arrived at 8222."},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "VoiceOutput", "messages": "You have arrived at 8222."},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        '',
        {"Action json Sequence": [{"robot": "Robot9"},{"skill": "GoTo", "object": "floorlamp"},{"skill": "Switchoff", "object": "floorlamp"},{"skill": "ReturnHome"}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "VoiceOutput", "messages": "I will take a picture in 5 seconds."},{"skill": "TakePicture"},{"skill": "SendPicture", "address": "010-1234-5678"},{"skill": "VoiceOutput", "messages": "Transmission is complete."}]},
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8324},{"skill": "VoiceOutput", "messages": "You have arrived at room 8324."},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot5"},{"skill": "StartCollabot"},{"skill": "OpenDrawer", "book": "Harry Potter"},{"skill": "ExecuteDrawerDetector"},{"skill": "CloseDrawer"},{"skill": "Reset"}]},
        {"Action json Sequence": [{"robot": "Robot4"},{"skill": "DriveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "DriveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "DriveTo", "location": 8222},{"skill": "Spray"},{"skill": "DriveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "DriveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "DriveTo", "location": 8100}]},
        {"Action json Sequence": [{"robot": "Robot8"},{"skill": "GoTo", "object": "Lettuce"},{"skill": "Pickup", "object": "Lettuce"},{"skill": "GoTo", "object": "CounterTop"},{"skill": "Put", "object": "Lettuce"},{"skill": "GoTo", "object": "Knife"},{"skill": "Pickup", "object": "Knife"},{"skill": "GoTo", "object": "CounterTop"},{"skill": "Slice", "object": "Lettuce"},{"skill": "Put", "object": "Knife"},{"skill": "ReturnHome"},{"robot": "Robot10"},{"skill": "GoTo", "object": "Mug"},{"skill": "Pickup", "object": "Mug"},{"skill": "GoTo", "object": "GarbageCan"},{"skill": "Throw", "object": "Mug"},{"skill": "ReturnHome"},{"robot": "Robot9"},{"skill": "GoTo", "object": "LightSwitch"},{"skill": "Switchoff", "object": "LightSwitch"},{"skill": "ReturnHome"}]}
    ]
    temp_answer = [ # 논문 test 할때 필요
        {"Action json Sequence": [{"robot": "Deli-Buddy"},{"skill": "MoveTo", "location": 8109},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray1"},{"skill": "MoveTo", "location": 8111},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray8"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "1floorev_front"},{"skill": "PreparetoCallElevator", "location": "1floorev_in"},{"skill": "CallElevator", "floor": "1", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "1floorev_in"},{"skill": "MoveElevator", "floor": "2"},{"skill": "MoveTo", "location": 8222},{"skill": "Detect", "direction": "right"},{"skill": "MoveRobotArm", "item": "tray9"},{"skill": "MoveTo", "location": 8205},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray6"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "2floorev_front"},{"skill": "PreparetoCallElevator", "location": "2floorev_in"},{"skill": "CallElevator", "floor": "2", "direction": "Up"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "2floorev_in"},{"skill": "MoveElevator", "floor": "3"},{"skill": "MoveTo", "location": 8323},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray2"},{"skill": "MoveTo", "location": 8304},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray3"},{"skill": "FoldRobotArm"},{"skill": "MoveTo", "location": "3floorev_front"},{"skill": "PreparetoCallElevator", "location": "3floorev_in"},{"skill": "CallElevator", "floor": "3", "direction": "Down"},{"skill": "CheckinsideElevator"},{"skill": "MoveTo", "location": "3floorev_in"},{"skill": "MoveElevator", "floor": "1"},{"skill": "MoveTo", "location": 8101},{"skill": "Detect", "direction": "left"},{"skill": "MoveRobotArm", "item": "tray5"},{"skill": "MoveTo", "location": 8100}]},
        '',
        '',
        '',
        '',
        '',
        '',
        '',
        {"Action json Sequence": [{"robot": "Robot6"},{"skill": "VoiceOutput", "messages": "I will take a picture in 5 seconds."},{"skill": "TakePicture"},{"skill": "SendPicture", "address": "010-1234-5678"},{"skill": "VoiceOutput", "messages": "Transmission is complete."},{"skill": "MoveTo", "location": 8100}]},
        '',
        '',
        {"Action json Sequence": [{"robot":"Robot3"},{"skill":"MoveTo","location":8222},{"skill":"CleanUp"},{"skill":"MoveTo","location":8200}]},
        ''
    ]

    correct = {1 : [-1,-1], 2 : [-1,-1], 3 : [-1,-1], 4: [-1,-1], 5 : [-1,-1], 6 : [-1,-1], 7 : [-1,-1], 8 : [-1,-1], 9 : [-1,-1], 10 : [-1,-1], 11 : [-1,-1], 12 : [-1,-1], 13 : [-1,-1]}
    
    for i in range(1,14):
        try_time = 0
        correct_time = 0
        print("test  : " + str(i) + "\n")
        for j in range(0,50):
            with open(f"/home/serverpc/server_backend/robot_taskmanager_llm/log/case3_50_2/test{i}_{j}.txt", "r") as f:
                example = f.read()
                # "2step output = " 이후부터 "runtime"까지 자르기
                start = example.find("2step output = ") + len("2step output = ")
                end = example.find("runtime")
                result = example[start:end].strip()
                jsondata = result
                # print(jsondata)
                
                if jsondata != '':
                    result = json.loads(jsondata)
                else:
                    result = jsondata
                
                try_time += 1
                if correct_answer_1[i-1] == result:
                    correct_time += 1
                    each_correct[i].append(1)
                    # print(each_correct)
                else:
                    each_correct[i].append(0)
                    # print(each_correct)
                    print("time : " + str(j))
                    print(jsondata)
                
            correct[i][0] = correct_time
            correct[i][1] = try_time
        print(correct)
        print(each_correct)