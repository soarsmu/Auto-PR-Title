import streamlit as st
import pyperclip
import requests
from bs4 import BeautifulSoup
from title_generator.model import get_model

def callback():
	st.session_state.submit_button = True
	st.session_state.title = None

def copy_callback(title):
	st.session_state.title = title

def parse_source(issue_urls, branch_url):
	# process issue url
	issue_title = set()
	commit_messages = set()
	issue_urls = issue_urls.split(',')

	for issue_url in issue_urls:
		issue_url = issue_url.replace("github.com", "api.github.com/repos")
		response = requests.get(issue_url)
		try:
			issue_title.add(response.json()['title'])
		except Exception as e:
			print(f"Requesting to {issue_url}")
			print(f"response: {response}")
			print(f"Exception: {e}")

	# process commits
	branch_url = branch_url.replace("github.com", "api.github.com/repos")
	response = requests.get(branch_url)
	try:
		commits = response.json()['commits']
	except Exception as e:
		print(f"Requesting to {issue_url}")
		print(f"response: {response}")
		print(f"Exception: {e}")

	for commit in commits:
		commit_message = commit['commit']['message']
		commit_messages.add(commit_message)
	return ' '.join(list(issue_title)), ' '.join(list(commit_messages))


def main(model):
	"""AutoPRTitle"""

	st.title("AutoPRTitle")
	menu=['Home', 'About']
	st.sidebar.write("🐹 This is a pull request generator tool for ICSME's paper <add_url>")
	
	with st.form(key='form1'):
		branch_url = st.text_input("Enter Branch Comparison URL", placeholder="branch comparison page (the URL can be obtained after clicking `New Pull Request` button)")
		issue_url = st.text_input("Enter Issue URL(s) (Optional)", placeholder="URL to the related issue(s), separated by comma `,`")
		description = st.text_area("Enter PR description (Optional)", placeholder="description")
		submit_button = st.form_submit_button(label='Generate PR Title', on_click=callback)

	if "submit_button" not in st.session_state:
		st.session_state.submit_button = False
	else:
		submit_button = True

	if submit_button:
		issue_title, commit_messages = parse_source(issue_url, branch_url)
		# title = issue_title + ' --- ' + commit_messages
		src = description + ' ' + commit_messages + ' ' + issue_title
		src = src.replace('\n', ' ')

		if "title" in st.session_state and st.session_state.title:
			title = st.session_state.title
			print(f"### USE CACHE")
		else:
			title = model.predict(src)
		# title = model.predict(src)
		print(f"""### title: {title}""")

		st.subheader("Generated PR Title: ")
		st.write(title)
		# copy_button = st.button("Copy", on_click=copy_callback(title))

		# if copy_button:
		# 	pyperclip.copy(title)
		# 	st.success("Copied!")


if __name__ == '__main__':
	model = get_model()
	main(model)