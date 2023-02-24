# colleges-api
API to get all the colleges in India

Here we have used the data from https://data.gov.in/catalog/list-colleges-aishe-survey 

## Requirements

* Python

### Searching a University

**GET:** */get/university/Mother Teresa*

**RESPONSE :**

```json
[
    {
        "Total Colleges in university": 11
    },
    [
        {
            "college_name": "Arulmigu Palaniandavar Arts College for Women, Palani (Id: C-17074)",
            "college_type": "Affiliated College",
            "district": "Dindigul",
            "state": "Tamil Nadu",
            "university": "Mother Teresa Women's University, Kodaikanal (Id: U-0466)"
        },
        {
            "college_name": "Govt., Arts College for Women, Nilakottai (Id: C-17042)",
            "college_type": "Affiliated College",
            "district": "Dindigul",
            "state": "Tamil Nadu",
            "university": "Mother Teresa Women's University, Kodaikanal (Id: U-0466)"
        },........

    ]
]
```

---------------------------------------

### Getting colleges in a State

**POST:** */get/state/*

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
        },...
       
    ]
]
```

 ---------------------------------------

### Getting colleges in a District

**POST:** */get/district/*

**Headers:** 

District - District to search

#### Example

**REQUEST :**
```
POST /colleges/district HTTP/1.1
HOST: localhost:5000
District: Dhule
```

**RESPONSE :**

```json
[
    {
        "Total Colleges in district": 79
    },
    [
        {
            "college_name": "D.S.Naik Ayurved Mahavidyalya, Dhule (Id: C-14037)",
            "college_type": "Affiliated College",
            "district": "Dhule",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "JMFs A.C.P.M. College B.Sc. Nursing, Dhule (Id: C-13741)",
            "college_type": "Affiliated College",
            "district": "Dhule",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "JMFs, A.C.P.M. College of Physiotherapy, Dhule (Id: C-13750)",
            "college_type": "Affiliated College",
            "district": "Dhule",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },
        {
            "college_name": "JMFs ACPM Dental College, Sakri Road, Dhule (Id: C-14024)",
            "college_type": "Affiliated College",
            "district": "Dhule",
            "state": "Maharashtra",
            "university": "Maharashtra University of Health Sciences, Nashik (Id: U-0313)"
        },...
    ]
]
```


##Contributers
* [Minhajshaikh321 ( Lead. Coordinator )](https://github.com/Minhajshaikh321)
* [Juned Chaudhary](https://github.com/jcjunaidchaudhary))


