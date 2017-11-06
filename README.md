# secretSanta
python code for Secret Santa that generates a random Secret Santa assignment then emails Santa who his/her gift recipient is.  For this I set up a vanilla gmail account for Santa.  Gmail uses SMTP.

config file is a json format that resembles:
'''{
    "gmailconfig":{
        "gmail_user":"",
        "gmail_password":""
    },
	"emailDict":{
		"kid1":"kid1@someemail.com",
		"kid2":"kid2@outlook.com",
		"kid3":"kid3@gmail.com"
    },
	"spouseDict":{
		"kid1":"Spouse1",
		"kid2":"Spouse2",
		"kid3":"none"
	},
	"other":{
		"kidList":[
			"kid1",
			"kid2",
			"kid3"]
	}

}'''


