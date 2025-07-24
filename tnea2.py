from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/3011")
def nit_trichy():
    return {
        "name": "National Institute of Technology, Tiruchirappalli",
        "location": "Tanjore Main Road, NH‑83, Tiruchirappalli",
        "dept": "CSE, ECE, ME, CE, EE, CHE, MME, ICE, Architecture",
        "phone_no": "0431‑2503000",
        "email": "admissions@nitt.edu",
        "counselling_no": "3011",
        "cutoff": {
            "CSE": "AIR ~15000",
            "ECE": "AIR ~18000",
            "ME": "AIR ~25000",
            "CE": "AIR ~28000",
            "EE": "AIR ~23000",
            "CHE": "AIR ~33000",
            "MME": "AIR ~34000",
            "ICE": "AIR ~27000",
            "Architecture": "NATA-based"
        }
    }

@app.get("/314")
def iiit_trichy():
    return {
        "name": "Indian Institute of Information Technology, Tiruchirappalli",
        "location": "Sethurapatti, Tiruchirappalli",
        "dept": "CSE, CSE (AI & DS), ECE, ECE (VLSI)",
        "phone_no": "9442045851",
        "email": "office@iiitt.ac.in",
        "counselling_no": "314",
        "cutoff": {
            "CSE": "AIR ~18000",
            "AI & DS": "AIR ~20000",
            "ECE": "AIR ~22000",
            "VLSI": "AIR ~25000"
        }
    }

@app.get("/3701")
def krct():
    return {
        "name": "K. Ramakrishnan College of Technology (KRCT)",
        "location": "Samayapuram, Tiruchirappalli",
        "dept": "CSE, AI & DS, IT, ECE, EEE, MECH, Civil",
        "phone_no": "0431-2670799",
        "email": "info@krct.ac.in",
        "counselling_no": "3701",
        "cutoff": {
            "CSE": "176.5",
            "AI & DS": "173.0",
            "IT": "172.0",
            "ECE": "170.0",
            "EEE": "168.0",
            "MECH": "160.0",
            "Civil": "158.0"
        }
    }

@app.get("/3830")
def krce():
    return {
        "name": "K. Ramakrishnan College of Engineering (KRCE)",
        "location": "Samayapuram, Tiruchirappalli",
        "dept": "CSE, IT, ECE, EEE, MECH, Civil",
        "phone_no": "0431-2670799",
        "email": "info@krce.ac.in",
        "counselling_no": "3830",
        "cutoff": {
            "CSE": "172.0",
            "IT": "170.0",
            "ECE": "165.0",
            "EEE": "160.0",
            "MECH": "157.0",
            "Civil": "155.0"
        }
    }

@app.get("/3819")
def saranathan():
    return {
        "name": "Saranathan College of Engineering",
        "location": "Panjappur, Tiruchirappalli",
        "dept": "CSE, AI & DS, IT, ECE, EEE, MECH, Civil",
        "phone_no": "8489915204",
        "email": "principal@saranathan.ac.in",
        "counselling_no": "3819",
        "cutoff": {
            "CSE": "180.0",
            "AI & DS": "175.0",
            "IT": "172.0",
            "ECE": "170.0",
            "EEE": "167.0",
            "MECH": "160.0",
            "Civil": "158.0"
        }
    }

@app.get("/3795")
def srm_trp():
    return {
        "name": "SRM TRP Engineering College",
        "location": "Tiruchirappalli",
        "dept": "CSE, AI & DS, ECE, EEE, MECH, Civil",
        "phone_no": "0431-2258080",
        "email": "info@srmtrep.edu.in",
        "counselling_no": "3795",
        "cutoff": {
            "CSE": "170.0",
            "AI & DS": "165.0",
            "ECE": "162.0",
            "EEE": "160.0",
            "MECH": "155.0",
            "Civil": "150.0"
        }
    }

@app.get("/3807")
def jjcet():
    return {
        "name": "J. J. College of Engineering & Technology",
        "location": "Ammapettai, Tiruchirappalli",
        "dept": "CSE, AI & DS, Cyber Security, ECE, MECH",
        "phone_no": "0431-2695606",
        "email": "principal@jjcet.ac.in",
        "counselling_no": "3807",
        "cutoff": {
            "CSE": "165.0",
            "AI & DS": "160.0",
            "Cyber Security": "158.0",
            "ECE": "160.0",
            "MECH": "150.0"
        }
    }

@app.get("/3465")
def gces():
    return {
        "name": "Government College of Engineering, Srirangam",
        "location": "Sethurapatti, Tiruchirappalli",
        "dept": "CSE, ECE, EEE, MECH, Civil",
        "phone_no": "9488008656",
        "email": "gcesrirangam@gmail.com",
        "counselling_no": "3465",
        "cutoff": {
            "CSE": "185.0",
            "ECE": "180.0",
            "EEE": "178.0",
            "MECH": "172.0",
            "Civil": "170.0"
        }
    }

@app.get("/3831")
def igce():
    return {
        "name": "Indra Ganesan College of Engineering",
        "location": "Manikandam, Tiruchirappalli",
        "dept": "CSE, IT, ECE, EEE, MECH, Civil, MBA, ME",
        "phone_no": "0431-2695500",
        "email": "info@igcengg.ac.in",
        "counselling_no": "3831",
        "cutoff": {
            "CSE": "158.0",
            "IT": "155.0",
            "ECE": "150.0",
            "EEE": "148.0",
            "MECH": "145.0",
            "Civil": "140.0"
        }
    }

@app.get("/3011")
def bit_trichy():
    return {
        "name": "Bharathidasan Institute of Technology (BIT - Anna University)",
        "location": "BIT Campus, Tiruchirappalli",
        "dept": "CSE, ECE, EEE, MECH, Civil, ICE",
        "phone_no": "0431-2407946",
        "email": "bitprincipal@annauniv.edu",
        "counselling_no": "3011",
        "cutoff": {
            "CSE": "188.0",
            "ECE": "180.0",
            "EEE": "175.0",
            "MECH": "172.0",
            "Civil": "170.0",
            "ICE": "168.0"
        }
    }
