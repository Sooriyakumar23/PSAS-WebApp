import streamlit as st
from PIL import Image
import datetime

st.set_page_config(page_title="PSAS-Web-App", page_icon=":computer:", layout="wide")

def main():
	st.title("PSAS-Dashboard")
	menu1 = ['Home', 'Login', 'Signup', 'Change credentials']
	choice1 = st.sidebar.selectbox('Menu', menu1)

	if choice1 == 'Login':
		st.subheader('Login section')

		username = st.sidebar.text_input('User Name')
		password = st.sidebar.text_input('Password', type='password')

		if st.sidebar.checkbox('Login'):
			with open('credentials.txt', 'r') as f:
				cred = f.read().split("\n")
			exist = False

			for elements in cred:
				element = elements.split(",")
				if (element[0] == username) and (element[1] == password):
					exist = True
					break

			if exist == True:		
				menu2 = ['Profile', 'Current', 'History']
				choice2 = st.sidebar.selectbox('Details', menu2)

				if choice2 == 'Profile':
					color = st.color_picker('Pick A Color', '#00f900')
					html_username = f'<p style="font-family:Courier; color:{color}; font-size: 50px;">User Name : {element[0]}</p>'
					html_password = f'<p style="font-family:Courier; color:{color}; font-size: 50px;">Password : {element[1]}</p>'
					html_uid = f'<p style="font-family:Courier; color:{color}; font-size: 50px;">Unique ID : {element[2]}</p>'

					st.markdown(html_username, unsafe_allow_html=True)
					st.markdown(html_password, unsafe_allow_html=True)
					st.markdown(html_uid, unsafe_allow_html=True)

				elif choice2 == 'Current':
					st.header('Current')

				elif choice2 == 'History':
					st.header('History')

			else:
				st.warning('Incorrect User Name / Password...')

		else:
			st.warning('Not logged in yet !')

	elif choice1 == 'Signup':
		st.subheader('Signup section')
		image = Image.open('signup.png')
		st.image(image)

		username = st.sidebar.text_input('User Name')
		password = st.sidebar.text_input('Password', type='password')
		confirm_password = st.sidebar.text_input('Confirm Password', type='password')
		uid = st.sidebar.text_input('Unique ID', type='password')

		if st.sidebar.checkbox('Signup'):
			if (username != '') and (password != '') and (confirm_password != '') and (uid != ''):
				if password != confirm_password:
					st.warning('Both passwords are not matched')
				else:
					with open('credentials.txt', 'r') as f:
						cred = f.read().split("\n")
					length = len(cred)
					count = 0
					for elements in cred:
						element = elements.split(",")
						if (element[0] == username) and (element[1] == password):
							st.warning('User Name / Password already exists. Try with new credentials.')
							break
						else:
							count += 1

					if count == length:
						with open('credentials.txt', 'a') as f:
							cred = '\n' + username + ',' + password + ',' + uid
							f.write(cred)
						st.write("Successfully signupped !")

			else:
				st.warning('Empty elements in the signup form')


	elif choice1 == 'Change credentials':
		st.subheader('Change credentials')
		image = Image.open('credentials.png')
		st.image(image)

		old_username = st.sidebar.text_input('Old User Name')
		old_password = st.sidebar.text_input('Old Password', type='password')

		new_username = st.sidebar.text_input('New User Name')
		new_password = st.sidebar.text_input('New Password', type='password')
		new_confirm_password = st.sidebar.text_input('Confirm New Password', type='password')
		new_uid = st.sidebar.text_input('Unique ID', type='password')

		if st.sidebar.checkbox('Change Credentials'):
			if new_password != new_confirm_password:
					st.warning('Both new passwords are not matched')
			else:
				with open('credentials.txt', 'r') as f:
					cred = f.read().split("\n")

				broke = False
				for elements in cred:
					element = elements.split(",")
					if (element[0] == old_username) and (element[1] == old_password):
						broke = True
						break

				if broke == True:
					cred.remove(element[0]+','+element[1]+','+element[2])
					if new_uid == '':
						new_uid = elements[-1]
					cred.append(new_username + ',' + new_password + ',' + new_uid)
					
					data = ''
					for i in cred:
						data += i
						data += '\n'
					with open('credentials.txt', 'w') as f:
						print (data[:-1])
						f.write(data[:-1])
					st.write('Successfully changed credentials !')

				else:
					st.warning('No such User Name / Password detected.')


	elif choice1 == 'Home':
		st.subheader('Welcome back to PSAS Home Section')
		image = Image.open('compuser.jpg')
		st.image(image, caption='A person who is working infront of a computer')
		color = st.color_picker('Pick A Color', '#00f900')
		quote = f'<p style="font-family:Courier; color:{color}; font-size: 20px;">We care you... You do your work...!</p>'
		st.markdown(quote, unsafe_allow_html=True)

if __name__ == '__main__':
	main()