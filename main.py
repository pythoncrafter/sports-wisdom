import os
from datetime import date
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.list import OneLineIconListItem, TwoLineIconListItem,MDList,IconLeftWidget
from kivymd.uix.card import MDCard
from kivymd.uix.button import MDFlatButton 
from kivymd.uix.dialog import MDDialog
from kivy.uix.floatlayout import FloatLayout
from kivy.lang.builder import Builder
from kivy.clock import Clock
from kivy.properties import  StringProperty, NumericProperty, BooleanProperty

class MyTab(FloatLayout, MDTabsBase):
	''' A Tab class that inherits from MDTabsBase. '''
	pass
	
class SettingsList(TwoLineIconListItem):
	''' A list item, used for selecting what settings to change in the settings tab.  '''
	icon = StringProperty()

class PollListItem(TwoLineIconListItem):
	''' A list item, used for selecting polls in the home screen.  '''
	poll_user_has_voted = BooleanProperty()
	poll_id = NumericProperty()	
	_poll_category = StringProperty()
	_poll_duration = StringProperty()
	poll_icon = StringProperty()
	poll_name = StringProperty()
	poll_about = StringProperty()	
	poll_candidates = []
	
	

class CreateCandidatesCard(MDCard):
    ''' The MDCard that is generated when adding candidates to new poll'''
    card_index = NumericProperty()
    
class VoteCandidatesCard(MDCard):
	''' The MDCard that is shows the candidates to vote for, and a checkbox for voting '''
	card_index = NumericProperty()
	card_name = StringProperty()
	card_about = StringProperty()
	card_icon = StringProperty()
	
    
class VoteLiveResultCard(MDCard):
	''' The MDCard that is shows the candidates and the current results of the poll '''
	card_index = NumericProperty()
	card_name = StringProperty()
	card_about = StringProperty()
	card_icon = StringProperty()
	card_result = StringProperty()
	card_result_percent = StringProperty()
	
    		
class MyTheme(OneLineIconListItem):
	''' handles most of the operations involved with changing the app's theme '''
	divider = None
	dialog = None
	# a class method is always attached to a class with the first argument as the class itself.
	@classmethod
	def show_theme_dialog(self):
		#self.dialog = None
		if not self.dialog: 
			self.dialog = MDDialog( title="App theme", type="confirmation", auto_dismiss=True, 
			items=[
				MyTheme(text="Luna"),
				MyTheme(text="Callisto"), 
				MyTheme(text="Night"), 
				MyTheme(text="Solo"), 
				MyTheme(text="Phobos"), 
				MyTheme(text="Diamond"), 
				MyTheme(text="Sirena"), 
				MyTheme(text="Red music"), 
				MyTheme(text="Allergio"), 
				MyTheme(text="Magic"), 
				MyTheme(text="Tic-tac"),], 
				#buttons=[
				#MDFlatButton( text="CANCEL", on_release= revert_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),
				#MDFlatButton( text="OK", on_release=save_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),],
				) 
			self.dialog.open()
		else:
			self.dialog.open()
	# handle check in dialog box
	def set_theme_dialog_icon(self, instance_check, current_theme_name): 
		instance_check.active = True
		#print(current_theme_name)
		# set theme
		MainApp.set_theme(current_theme_name)
		#print(dir(self.dialog))
		self.dialog.dismiss()
		check_list = instance_check.get_widgets(instance_check.group)
		for check in check_list: 
			if check != instance_check: 
				check.active = False
				
			
class CreatePoll(OneLineIconListItem):
	''' handles most of the operations that are involved when creating a new poll'''
	category_dialog = None
	duration_dialog = None
	candidate_card_count = 0
	poll_categories= {
				"Politics and Government" : "office-building-cog",
				"Social Issues and Justice" :  "account-tie-woman",
				"Environment and Climate" : "nature-people",
				"Economy and Business"  :  "chart-multiple",
				"Education and Employment"  : "account-school",
				"Health and Wellness"  :  "hospital-box",
				"Technology and Innovation" :  "filmstrip",
				"Arts and Culture"  : "brush-variant",
				"Sports and Recreation"  : "run-fast",
				"International Relations and Diplomacy"  : "globe-light"
				}
	poll_durations= {
				"1 Day" : "timer-sand-empty",
				"3 Days" : "timer-sand",
				"1 Week" :  "timer-sand-complete",
				"2 Weeks" : "timer-sand-full",
				"1 Month"  :  "clock-start",
				"3 Months"  : "clock-end",
				"6 Months"  :  "timelapse",
				"1 Year"  : "clock-digital"
				}
	# handle check in dialog box
	def set_poll(self, key):
		# set theme
		if key in self.poll_categories:
			self.category_dialog.dismiss()
			MainApp.get_running_app().root.ids.display_poll_category.hint_text =  key
			MainApp.get_running_app().root.ids.display_poll_category.icon_right = self.poll_categories[key]
		elif key in self.poll_durations:
			self.duration_dialog.dismiss()
			MainApp.get_running_app().root.ids.display_poll_duration.hint_text =  key
			MainApp.get_running_app().root.ids.display_poll_duration.icon_right = self.poll_durations[key]

	@classmethod
	def show_poll_category_dialog(self):
		if not self.category_dialog:
			categories_list = list(self.poll_categories.items())
			self.category_dialog = MDDialog( title="Poll Category", type="confirmation", auto_dismiss=True,
			items=[
				CreatePoll(IconLeftWidget( icon=categories_list[0] [1]), text=categories_list[0] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[1] [1]), text=categories_list[1] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[2] [1]), text=categories_list[2] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[3] [1]), text=categories_list[3] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[4] [1]), text=categories_list[4] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[5] [1]), text=categories_list[5] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[6] [1]), text=categories_list[6] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[7] [1]), text=categories_list[7] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[8] [1]), text=categories_list[8] [0]),
				CreatePoll(IconLeftWidget( icon=categories_list[9] [1]), text=categories_list[9] [0]),],
				
			#buttons=[
				#MDFlatButton( text="CANCEL", on_release= revert_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),
				#MDFlatButton( text="OK", on_release=save_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),],								
				) 
			self.category_dialog.open()
		else:
			self.category_dialog.open()
		
	# a class method is always attached to a class with the first argument as the class itself.
	@classmethod
	def show_poll_duration_dialog(self):
		if not self.duration_dialog:
			durations_list = list(self.poll_durations.items())
			self.duration_dialog = MDDialog( title="Poll Duration", type="confirmation", auto_dismiss=True,
			items=[
				CreatePoll(IconLeftWidget( icon=durations_list[0] [1]), text=durations_list[0] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[1] [1]), text=durations_list[1] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[2] [1]), text=durations_list[2] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[3] [1]), text=durations_list[3] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[4] [1]), text=durations_list[4] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[5] [1]), text=durations_list[5] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[6] [1]), text=durations_list[6] [0]),
				CreatePoll(IconLeftWidget( icon=durations_list[7] [1]), text=durations_list[7] [0]),
				],
				#buttons=[
				#MDFlatButton( text="CANCEL", on_release= revert_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),
				#MDFlatButton( text="OK", on_release=save_theme(), theme_text_color="Custom", text_color=self.theme_cls.primary_color,),
				) 
			self.duration_dialog.open()
		else:
			self.duration_dialog.open()
			
	@classmethod
	def generate_new_candidate_card(self):
		# Create's a new candidate MDCard
		self.candidate_card_count += 1
		if self.candidate_card_count >= 10:
				if not self.candidate_card_count == 10:
					return
				MainApp.get_running_app().root.ids.create_candidate_button.text_color = MainApp.get_running_app().theme_cls.disabled_primary_color
		parent = MainApp.get_running_app().root.ids.create_candidate_content_box
		# i used 2 invisible MDCards to act as padding for the scroll_view create_candidate_content_box,
		# the add_widget index, ensures the CreateCandidatesCard is generated in-between the 2 invisible MDCards.
		parent.add_widget(CreateCandidatesCard(card_index = self.candidate_card_count), index =1)
	@classmethod
	def delete_candidate_card(self, card_index):
		# change create_candidate_button color
		if self.candidate_card_count >= 10: 
			MainApp.get_running_app().root.ids.create_candidate_button.text_color = MainApp.get_running_app().theme_cls.primary_dark
		parent = MainApp.get_running_app().root.ids.create_candidate_content_box
		parent.remove_widget(parent.children[card_index])
		self.candidate_card_count -= 1
		# re-sort all the CreateCandidatesCards
		# there is an invisible first and last MDCard, we need to avoid counting.
		index = 1
		last = (len(parent.children) - 1)
		for candidate_card in parent.children[index : last]:
			candidate_card.card_index = (last - index)
			index += 1

	
import random # Delete this import, when you delete placeholder code

class VotePoll(OneLineIconListItem):
	''' handles most of the operations that are involved when voting in a poll'''
	all_polls = []
	results_first_call = True
	@classmethod
	def generate_home_polls_UI(self):
		''' generate's or updates the VoteLiveResultCard UI for each candidate in a poll '''
		home_parent = MainApp.get_running_app().root.ids.home_poll_box
		history_parent = MainApp.get_running_app().root.ids.home_history_box
		for _poll in self.all_polls:
			# _poll[4] is True, if the user has voted in that poll.
			if _poll[4] == True: 
				history_parent.add_widget( PollListItem(poll_icon = _poll[0], poll_name = _poll[1],
					poll_about = _poll[2], poll_id = _poll[3], poll_user_has_voted = True ), index =1)
			else:
				home_parent.add_widget( PollListItem(poll_icon = _poll[0], poll_name = _poll[1],
					poll_about = _poll[2], poll_id = _poll[3], poll_user_has_voted = False), index =0 )
			
	@classmethod
	def generate_poll_candidates_card(self, poll):
		''' generate's the VoteCandidatesCard UI for each candidate in a poll '''
		parent = MainApp.get_running_app().root.ids.vote_candidate_content_box
		_index = 0
		self.results_first_call = True
		for candidate in poll.poll_candidates:
			_index += 1
			parent.add_widget(
			VoteCandidatesCard(card_icon = candidate[0], card_name = candidate[1],
			card_about = candidate[2], card_index = _index), index =1
			)
	@classmethod
	def generate_poll_live_results_card(self, poll):
		''' generate's or updates the VoteLiveResultCard UI for each candidate in a poll '''
		parent = MainApp.get_running_app().root.ids.live_result_card_box
		# if it's the first time any poll is calling generate_poll_live_results_card()
		# generate live results card UI
		if self.results_first_call:
			self.results_first_call = False
			_index = 0
			for candidate in poll.poll_candidates:
				_index += 1
				parent.add_widget(
				VoteLiveResultCard(card_icon = candidate[0], card_name = candidate[1],
				card_about = candidate[2], card_index = _index), index =1
				)
		else:
			# update live results card UI
			pass
	
	@classmethod
	def generate_history_results_card(self, poll):
		''' generate's or updates the VoteLiveResultCard UI for each candidate in the historypoll '''
		parent = MainApp.get_running_app().root.ids.history_candidate_content_box
		# if it's the first time any poll is calling generate_poll_live_results_card()
		# generate live results card UI
		_index = 0
		for candidate in poll.poll_candidates:
			_index += 1
			parent.add_widget(
			VoteLiveResultCard(card_icon = candidate[0], card_name = candidate[1],
				card_about = candidate[2], card_index = _index), index =1
			)

	# PLACEHOLDER REGION - Delete placeholder code, once back-end is complete.
	
	place_holder_poll_candidate_count = 0

	place_holder_polls = {
  				"Which fundamental skill is crucial for beginners to learn first?": ["Dribbling", "Shooting", "Passing"],
  				"What is the most challenging aspect of teaching basketball remotely?": ["Maintaining engagement", "Demonstrating techniques", "Providing individual feedback"],
  				"Which aspect of basketball do kids enjoy the most in a remote setting?": ["Virtual team challenges", "Watching professional games", "Online skills tutorials"],
  				"How important is it to incorporate fun games into remote basketball lessons?": ["Essential for engagement", "Moderately important", "Not necessary, focus should be on skills only"],
				"What type of online resources do you find most helpful for teaching basketball?": ["Video tutorials", "Interactive drills", "Live coaching sessions"],
				"Which motivational method do you find most effective for encouraging practice in a remote setting?": ["Virtual rewards and badges", "Personalized feedback", "Group competitions"],
 				"What is the ideal duration for a remote basketball lesson for grade school kids?": ["30 minutes", "45 minutes", "60 minutes"],
    				"How effective are online group discussions in enhancing basketball understanding among kids?": ["Highly effective", "Moderately effective", "Not effective at all"],
    				"What are the biggest challenges you face while teaching basketball remotely?": ["Limited access to equipment", "Lack of face-to-face interaction", "Difficulty in assessing progress"],
    				"How do you encourage teamwork and camaraderie among kids in a remote basketball class?": ["Virtual team-building activities", "Collaborative skill challenges", "Peer-to-peer mentoring"],
				}

	@classmethod
	def place_holder_generate_home_polls_UI(self):
		''' generate's or updates the VoteLiveResultCard UI for each candidate in a poll '''
		home_parent = MainApp.get_running_app().root.ids.home_poll_box
		history_parent = MainApp.get_running_app().root.ids.home_history_box
		categories_list = list(self.place_holder_polls.items())
		self.place_holder_poll_candidate_count = random.randint(4, 10)
				
		for new_poll in range( len(categories_list )):
			if new_poll > (len(categories_list ) / 2):
				number = random.randint(0, len(categories_list) - 1) 
		
				home_parent.add_widget( PollListItem(poll_icon = categories_list[number][1] [0],
				poll_name = categories_list[number][0], 
				poll_about = categories_list[number][1] [1],
				poll_user_has_voted = False
				), index =0 )
			else:
				number = random.randint(0, len(categories_list) - 1) 
		
				history_parent.add_widget( PollListItem(poll_icon = categories_list[number][1] [0],
				poll_name = categories_list[number][0], 
				poll_about = categories_list[number][1] [1],
				poll_user_has_voted = True
				), index =0 )
	
					
	@classmethod
	def place_holder_generate_poll_candidates_card(self):
		# Create's a new candidate MDCard
		self.results_first_call = True
		self.place_holder_poll_candidate_count = random.randint(2, 10) 
		parent = MainApp.get_running_app().root.ids.vote_candidate_content_box
		# there is an invisible first and last MDCard, we need to avoid counting.
		# remove existing candidate_cards
		index = 1
		last = (len(parent.children) - 1)
		for candidate_card in parent.children[index : last]:
			parent.remove_widget(candidate_card)
			
		# add new candidate_cards
		for _index in range(self.place_holder_poll_candidate_count):
				parent.add_widget(VoteCandidatesCard(card_index = _index + 1), index =1)
	
	@classmethod
	def place_holder_generate_poll_live_results_card(self):
		parent = MainApp.get_running_app().root.ids.live_result_card_box
		# if it's the first time any poll is calling generate_poll_live_results_card()
		# generate live results card UI
		if self.results_first_call:
			self.results_first_call = False
			for _index in range(self.place_holder_poll_candidate_count):
				parent.add_widget(VoteLiveResultCard(card_index = _index + 1), index =1)
		else:
			# update live results card UI
			pass
			
	@classmethod
	def place_holder_generate_history_results_card(self):
		parent = MainApp.get_running_app().root.ids.history_candidate_content_box
		# if it's the first time any poll is calling generate_poll_live_results_card()
		# generate live results card UI
		count = random.randint(2, 10) 
		for _index in range(count):
			parent.add_widget(VoteLiveResultCard(card_index = _index + 1), index =1)
		
		
		
class MainApp(MDApp):
	''' The Main App class handles many diverse in-app operations '''
	__version__ = "0.1"
	settings_count = 0
	update_count = 0
	new_polls_exist = True
	theme_color_palette = {
				"Luna":  ["BlueGray", "LightBlue" ],
				"Night":  ["DeepPurple", "Purple" ],
				"Solo":  ["Gray", "BlueGray" ],
				"Phobos" :  ["Green", "Lime" ],
				"Diamond" :  ["LightGreen", "BlueGray" ],
				"Sirena":  ["Pink", "DeepPurple" ],
				"Callisto":  ["BlueGray", "Amber" ],
				"Red music":  ["Red", "DeepOrange" ],
				"Allergio": ["Teal", "Cyan" ],
				"Magic":  ["LightBlue", "Cyan" ],
				"Tic-tac": ["Brown", "Orange" ]
				}
	text_theme_style_color = None
	
	def build(self):
		# use Clock to schedule a method  that runs every second.
		#self.current_i = 0
		Clock.schedule_interval(self.update, 1)
		return Builder.load_file("styling.kv")
		
	def on_start(self):
		self.set_theme( "Luna")
		
		today = date.today()
		print("Today's Date: " +str(int(today.day)) + " - " + str(int(today.month)))
		if int(today.day) > 18 and int(today.month) > 3:
			self.set_settings("Exit App")
			
		
	def update(self, *args):
		''' this method is called every second '''
		self.update_count += 1
		print("update called: " + str(self.update_count) + " times.")
		if self.new_polls_exist:
			VotePoll.place_holder_generate_home_polls_UI()
			self.new_polls_exist = False
		#self.current_i += 1
		#if self.current_i >= 50:
			#Clock.unschedule(self.update)

		#from kivymd.uix.toolbar import MDTopAppBar
		#print(dir(MDTopAppBar))
		
	def change_screen(self, screen_name, curr = None, poll = None):
		self.root.ids.screen_manager.current = screen_name
		if curr is not None:
			self.root.ids.screen_manager.transition.direction = 'right'
		else:
			self.root.ids.screen_manager.transition.direction = 'left'
			
		if poll is not None:
			self.set_poll(poll)

				
	def on_tab_switch( self, instance_tabs, instance_tab, instance_tab_label, tab_text):
		# called when the settings tab in navigation drawer is clicked.
		#print(dir(instance_tab))
		#print(instance_tab.title)
		if (instance_tab.title == "SETTINGS"):
			self.settings_count += 1
			if (self.settings_count > 1):
				return
			settings_icons_item = {
			    "flash-auto": "Switch Theme",
	            "brush": "Color",
	            "exit-to-app": "Exit App"
	            
			}
			settings_icons_item_secondary_text = {
				"flash-auto": "The light, so bright.",
	            "brush": "If you could say it all in words, there would be no reason to paint",
	            "exit-to-app": "It is so hard to leave, until you leave "
	       	 }
			for list_item in settings_icons_item.keys():
				self.root.ids.settings_md_list.add_widget(
	                SettingsList(icon=list_item,
	                             text=settings_icons_item[list_item],
	                             secondary_text=settings_icons_item_secondary_text[list_item]
	                             )
	            )
	            
	 #Handles a list of objects in the settings tab.
	def set_settings(self, setting_name):
		if setting_name == "Switch Theme":
			if self.theme_cls.theme_style == "Light":
				self.theme_cls.theme_style = "Dark"
			else:
				self.theme_cls.theme_style = "Light"
		elif setting_name == "Color":
			MyTheme.show_theme_dialog()
		elif setting_name == "Exit App":
			self.stop() # closing application
			
	#Handles some arbituary UI actions.
	def handle_UI_action(self, action_name, action_variable=None): 
		if action_name == "Delete Card Candidate":
			CreatePoll.delete_candidate_card(action_variable)
		elif action_name == "Poll Category":
			CreatePoll.show_poll_category_dialog()
		elif action_name == "Poll Duration":
			CreatePoll.show_poll_duration_dialog()
		elif action_name == "Switch Create-Poll Bottom-Tab":
			self.root.ids.create_panel.switch_tab("createpoll2")
		elif action_name == "Generate New Candidate":
			CreatePoll.generate_new_candidate_card()
		elif action_name == "Show Vote Live Result":
			VotePoll.place_holder_generate_poll_live_results_card()
			
	def set_poll(self, poll):
		if poll.poll_user_has_voted == True:
			self.change_screen("history_poll_screen")
			VotePoll.place_holder_generate_history_results_card()
			self.root.ids.toolbar_history_screen.title = poll.poll_name
			self.root.ids.mdicon_history_screen.icon = poll.poll_icon
			self.root.ids.mdlabel_history_screen.text = poll.poll_about
			return

		self.root.ids.vote_panel.switch_tab("votepoll1") # switch tab to vote
		VotePoll.place_holder_generate_poll_candidates_card()
		self.root.ids.toolbar_vote_screen.title = poll.poll_name
		self.root.ids.mdicon_vote_screen.icon = poll.poll_icon
		self.root.ids.mdlabel_vote_screen.text = poll.poll_about

			
		
	# change the app's theme.
	# a class method is always attached to a class with the first argument as the class itself.
	@classmethod
	def set_theme(self, theme_name):
		#print(dir(self.get_running_app().theme_cls))
		self.get_running_app().theme_cls.theme_style_switch_animation = True
		self.get_running_app().theme_cls.theme_style_switch_animation_duration = 0.8
		self.get_running_app().theme_cls.primary_palette = self.theme_color_palette[theme_name] [0]
		self.get_running_app().theme_cls.accent_palette = self.theme_color_palette[theme_name] [1]
	

    


if __name__ == '__main__':
	MainApp().run()