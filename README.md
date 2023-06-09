# DiscordEmailOsint
Python script that automates an API post request to check if an email has been registered with a given email. It can also take in a .txt file containing a list of email addresses with a new line for each.


### Usage

Ensure json, sys & requests library are installed

`pip install requests sys json argparse`

`chmod +x check_email.py`

`./check_email.py --email emailToBeChecked@domain.com`

`./check_email.py --file emails.txt` 

or

`python check_email.py --email emailToBeChecked@domain.com`

### How it works

When registering on the discord website, an API POST call to discord.com/api/v9/auth/register is made with the following data fields:

- email
- username
- password
- invite
- consent
- date_of_birth
...

If the account is registered the following response will be returned:

`{
	"code": 50035,
	"errors": {
		"email": {
			"_errors": [
				{
					"code": "EMAIL_ALREADY_REGISTERED",
					"message": "Email is already registered."
				}
			]
		}
	},
	"message": "Invalid Form Body"
}`





