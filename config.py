import cv2

cfg = {
    "screen_x": 1280,
    "screen_y": 720,
    "min_detection_confidence": 0.65, 
    "min_tracking_confidence": 0.65, 
    "max_num_hands": 1,
    "tolerance": 0.5, 
    "alpha": 0.75, 
    "btnClickDelay": 1.5, 
    "btnclr" : (105,105,105), 
    "txtclr" : (255,255,255), 
    "btnparams": {
        "W": 400, 
        "H": 80, 
        "BtnSp": 20, 
        "R": 40, 
        "CirSp": 50 
    },
    "txtparams": {

        "xadj": +20,
        "yadj": -20,
        "font": cv2.FONT_HERSHEY_SIMPLEX,
        "fontScale": 1.8,
        "thickness": 2
    },
    "currentpage": "FaceRec",
    "sqlitepage": "db_connector",
    "pages": {
        "FaceRec":{
            "pagetitle":["Select Match to match your face and Login", 100, 1.5, (60,216,65), 4],
            "buttons": ["","","","","","","","Match"],
            "navigation": ["","","","","","","","Match"]
        },
        "Transactions":{
            "pagetitle": ["Select Any Transaction", 150, 2, (255,0,0), 4],
            "buttons":["Withdraw", "Balance", "Transfer", "Deposit", "", "" , "Exit", ""],
            "navigation": ["Withdraw-SelAccType", "Balance-SelAccType", "Transfer-SelAccType",
                           "Deposit-SelAccType", "", "", "Exit", ""]
        },

        "Withdraw-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking", "", "Credit"],
            "navigation": ["", "SelectAmountW", "", "SelectAmountW", "", "SelectAmountW"]
        },
        "SelectAmountW": {
            "pagetitle": ["Select Amount to Withdraw", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["ReceiptW","ReceiptW","ReceiptW","ReceiptW"]
        },
        "ReceiptW": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["WDDoneR", "", "WDDone"]
        },
        "WDDoneR": {
            "pagetitle": ["Please take your Card, Cash, & Receipt", 150, 1.8, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "WDDone": {
            "pagetitle": ["Please take your Card & Cash", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Balance Enquiry transaction
        "Balance-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking"],
            "navigation": ["", "ReceiptBL", "", "ReceiptBL"]
        },
        "ReceiptBL": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["ReceiptGen", "", "BLDone"]
        },
        "ReceiptGen" : {
            "pagetitle": ["Your Savings Account Balance", 150,2,(255,0,0),4],
            "buttons": ["Ok"],
            "navigation": ["BLDone"]
        },
        "BLDone": {
            "pagetitle": ["Your Balance is Rs.5000.", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Transfer transaction
        "Transfer-SelAccType" : {
            "pagetitle": ["Select Transfer Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Sav>Check", "", "Check>Sav"],
            "navigation": ["", "SelectAmountT", "", "SelectAmountT"]
        },
        "SelectAmountT": {
            "pagetitle": ["Select Amount to Transfer", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["ReceiptT","ReceiptT","ReceiptT","ReceiptT"]
        },
        "ReceiptT": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["TDoneR", "", "TDone"]
        },
        "TDoneR": {
            "pagetitle": ["Your Transfer was Successful! Please take Receipt.", 150, 1.5, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "TDone": {
            "pagetitle": ["Your Transfer was Successful!", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },

        # All the pages for Deposit transaction
        "Deposit-SelAccType" : {
            "pagetitle": ["Select Account Type", 150, 2, (255,0,0), 4],
            "buttons":["", "Savings", "", "Checking"],
            "navigation": ["", "SelectAmountD", "", "SelectAmountD"]
        },
        "SelectAmountD": {
            "pagetitle": ["Select Amount to Deposit", 150, 2, (255,0,0), 4],
            "buttons":["Rs.100", "Rs.200", "Rs.500", "Rs.2000"],
            "navigation": ["Deposit","Deposit","Deposit","Deposit"]
        },
        "Deposit":{
            "pagetitle": ["Please Insert the Money", 150, 2, (255,0,0), 4],
            "buttons": ["","","","","","","","Done"],
            "navigation": ["","","","","","","","ReceiptD"]
        },
        "ReceiptD": {
            "pagetitle": ["Do you want a Receipt?", 150, 2, (255,0,0), 4],
            "buttons":["Yes", "", "No"],
            "navigation": ["DDoneR", "", "DDone"]
        },
        "DDoneR": {
            "pagetitle": ["Your Deposit was Successful! Please take Receipt.", 150, 1.5, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        },
        "DDone": {
            "pagetitle": ["Your Deposit was Successful!", 150, 2, (255,0,0), 4],
            "buttons":["", "", "", "", "", "", "New Txn", "Done"],
            "navigation": ["", "", "", "", "", "", "Transactions", "Exit"]
        }
    }
}