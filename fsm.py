from transitions.extensions import GraphMachine

class TocMachine(GraphMachine):

    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
		
    #start    
    def is_start_talking(self, update):
        text = update.message.text        
        return text.lower() == 'hello'
		   
    def is_back(self, update):
        text = update.message.text        
        return text.lower() == 'leave'
		
	#state1	
    def is_going_to_state1(self, update):
        text = update.message.text
        return text.lower() == 'simple'
           		
    def is_going_to_state11(self, update):
        text = update.message.text
        if text.lower() != '87' :
           update.message.reply_text("wrong~Try again ")
           return False
        else :
           return True
		
    def is_going_to_state12(self, update):
        text = update.message.text
        if text.lower() != '9487' :
           update.message.reply_text("Wrong~Try again ")
           return False
        else :
           return True
		
    def is_going_to_state13(self, update):
        text = update.message.text
        if text.lower() != '5487' :
           update.message.reply_text("Wrong~Try again ")
           return False
        else :
           return True
	
		
	#state2	
    def is_going_to_state2(self, update):
        text = update.message.text
        return text.lower() == 'medium'
		
    def is_going_to_state21(self, update):
        text = update.message.text
        if text.lower() != '7' :
           update.message.reply_text("Wrong~Try again ")
           return False
        else :
           return True
		
    def is_going_to_state22(self, update):
        text = update.message.text
        if text.lower() != '74' :
           update.message.reply_text("Wrong~Try again")
           return False
        else :
           return True

    def is_going_to_state23(self, update):
        text = update.message.text
        if text != "I'm stupid" :
           update.message.reply_text("Wrong~Try again")
           return False
        else :
           return True
		
	#state3
    def is_going_to_state3(self, update):
        text = update.message.text
        return text.lower() == 'hard'
		
    def is_going_to_state31(self, update):
        text = update.message.text
        if text.lower() != '13' :
           update.message.reply_text("Wrong~Try again")
           return False
        else :
           return True
		
    def is_going_to_state32(self, update):
        text = update.message.text
        if text.lower() != 'b' :
           update.message.reply_text("Wrong~Try again")
           return False
        else :
           return True

    def is_going_to_state33(self, update):
        text = update.message.text
        if text.lower() != '7' :
           update.message.reply_text("Wrong~Try again")
           return False
        else :
           return True
		
	#init	
    def on_enter_user(self, update):
        update.message.reply_text("Hi~This is a question game.\n Choose 'simple','medium'or 'hard', or choose to 'leave'")
		
		
    def on_enter_startstate(self, update):
        update.message.reply_text("You've leave, if you want to start again just say hello to me~")

	#state1		
    def on_enter_state1(self, update):
        update.message.reply_text("Ok, this is a arithmetic question list.For warming up,determine \n360/(1+2+3)+243/9")

    def on_exit_state1(self, update):
        print('Leaving state1')
		
    def on_enter_state11(self, update):
        update.message.reply_text("Correct~360/(1+2+3)+243/9=87")
        update.message.reply_text("Next~Determine \n87*200-320*25+250/(2+3)+259/7")

    def on_exit_state11(self, update):
        print('Leaving state11')

    def on_enter_state12(self, update):
        update.message.reply_text("Correct~Answer is 9487")
        update.message.reply_text("Last question~Determine \n74*74+1331/121")
        self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')

    def on_enter_state13(self, update):
        update.message.reply_text("恩，自己知道就好")
        self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')
		

	#state2		
    def on_enter_state2(self, update):
        update.message.reply_text("Ok, this will be a answer-what-you-see question.\nFirst, how many circles are in this picture?")
        update.message.reply_photo(photo=open('pic/p1.png', 'rb'))

		   
    def on_exit_state2(self, update):
        print('Leaving state2')
		
    def on_enter_state21(self, update):
        update.message.reply_text("Correct~Next, enter the number you see")
        update.message.reply_photo(photo=open('pic/p2.jpg', 'rb'));
		   
    def on_exit_state21(self, update):
        print('Leaving state21')
		
    def on_enter_state22(self, update):
        update.message.reply_text("Correct~Next, Please enter the origianl text (changed by mirror)")
        update.message.reply_photo(photo=open('pic/p3.png', 'rb'))
        self.go_back(update)
		   
    def on_exit_state22(self, update):
        print('Leaving state22')

    def on_enter_state23(self, update):
        update.message.reply_text("恩~我知道。")
        self.go_back(update)
		   
    def on_exit_state23(self, update):
        print('Leaving state23')
    
	#state3
    def on_enter_state3(self, update):
        update.message.reply_text("Well, this is a listening test game, Q1. how many notes do you hear in the following audio file?")
        update.message.reply_audio(audio=open('mp3/Q1.mp3', 'rb'))
		   
    def on_exit_state3(self, update):
        print('Leaving state3')
		
    def on_enter_state31(self, update):
        update.message.reply_text("Correct~Next, listening to the average notes, how fast is it?")
        update.message.reply_text("(a)225notes per minutes\n(b)156notes per minutes\n(c)138notes per minutes\n(enter 'a' 'b' or 'c')")
        update.message.reply_audio(audio=open('mp3/Q2.mp3', 'rb'))
        
		   
    def on_exit_state31(self, update):
        print('Leaving state31')
		
    def on_enter_state32(self, update):
        update.message.reply_text("Correct~Last, listening to the music clip, what's the time signature of this riff?")
        update.message.reply_text("__  /  4  \n(fill the blank)")
        update.message.reply_audio(audio=open('mp3/Q3.mp3', 'rb'))
		   
    def on_exit_state32(self, update):
        print('Leaving state32')		
		
    def on_enter_state33(self, update):
        update.message.reply_text("沒想到你竟然能答對，就不罵你了")
        self.go_back(update)
		   
    def on_exit_state32(self, update):
        print('Leaving state33')		
		
