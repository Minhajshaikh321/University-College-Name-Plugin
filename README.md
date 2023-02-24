# colleges-api
API to get all the colleges in India

Here we have used the data from https://data.gov.in/catalog/list-colleges-aishe-survey 

## Requirements

* Python

## Note

* If you want to verfify below data check it out in database1.csv also you can go through api testing



### Listing total number of colleges by university name

**GET:** */get/university/Goa*

**RESPONSE :**

```json
[
    {
        "Total Colleges in university": 65
    },
    [
        {
            "college_name": "AGNEL INSTITUTE OF TECHNOLOGY AND DESIGN, ASSAGAO, BARDEZ (Id: C-46329)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Carmel College of Arts Science & Commerce for Women (Id: C-33103)",
            "college_type": "Affiliated College",
            "district": "South Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Centre for Latin American Studies (Id: C-30837)",
            "college_type": "PG Center / Off-Campus Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Centre for Women's Studies (Id: C-30871)",
            "college_type": "PG Center / Off-Campus Center",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Dempo Charities Trusts S.S. Dempo College of Commerce & Economics Altinho (Id: C-30828)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
        {
            "college_name": "Devi Sharvani Education Societys V.M. Salgaocar College of Law Miramar Panaji (Id: C-30825)",
            "college_type": "Affiliated College",
            "district": "North Goa",
            "state": "Goa",
            "university": "Goa University, Goa (Id: U-0121)"
        },
    
    ]
]
```

---------------------------------------

### Searching a College by state

**POST:** */get/state/Sikkim*

**REQUEST :**
```
POST /colleges/search HTTP/1.1
HOST: localhost:5000
 ```

**RESPONSE :**

```json
[
    {
        "Total Colleges in state": 20
    },
    [
        {
            "college_name": "College of Agricultural Engineering and Post Harvest Technology, Ranipool, Gangtok (Id: C-26829)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Central Agricultural University, Imphal (Id: U-0336)"
        },
        {
            "college_name": "School of Basic & Applied Sciences (SBAS) (Id: C-8628)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal College of Nursing (SMCON) (Id: C-8624)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
        {
            "college_name": "Sikkim Manipal College of Physiotherapy (SMCOP) (Id: C-8626)",
            "college_type": "Constituent / University College",
            "district": "East District",
            "state": "Sikkim",
            "university": "Sikkim Manipal University, Gangtok (Id: U-0431)"
        },
    ]
]
```

---------------------------------------

### Getting colleges in a District

**GET:** */get/district/Dima*

**Headers:** 

State - State to search

#### Example

**REQUEST :**
```
HOST: localhost:5000
State: Dima Hasao
 ```

**RESPONSE :**

```json
[
    {
        "Total Colleges in district": 2
    },
    [
        {
            "college_name": "J.B.Hagjer Degree College (Id: C-26440)",
            "college_type": "Affiliated College",
            "district": "Dima Hasao",
            "state": "Assam",
            "university": "Assam University, Silchar (Id: U-0050)"
        },
        {
            "college_name": "Rangsina College (Id: C-26392)",
            "college_type": "Affiliated College",
            "district": "Dima Hasao",
            "state": "Assam",
            "university": "Assam University, Silchar (Id: U-0050)"
        }
    ]
]
```

 ---------------------------------------

### Getting colleges in a College Type(Affiliated College,Constituent / University College,Recognized Center,PG Center/Off-Campus)

**POST:** */get/collegetype/*



#### Example

**REQUEST :**
```
HOST: localhost:5000
College Type: Consituent
Offset: 0
```

**RESPONSE :**

```json
[
    {
        "college_name": "University COllege of Arts, Commerce and Law (Id: C-32637)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Engineering & Technology (Id: C-32695)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Pharmaceutical Sciences (Id: C-32766)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University College of Physical Education and Sports Sciences (Id: C-32653)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University Collge of Architecture & Planning (Id: C-32723)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
    {
        "college_name": "University Collge of Sciences (Id: C-32742)",
        "college_type": "Constituent / University College",
        "district": "Guntur",
        "state": "Andhra Pradesh",
        "university": "Acharya Nagarjuna University, Guntur (Id: U-0003)"
    },
]
```

---------------------------------------


##Contributers
* [Minhajshaikh321 ](https://github.com/Minhajshaikh321)
* [jcjunaidchaudhary](https://github.com/jcjunaidchaudhary)




