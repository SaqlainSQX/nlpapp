from tkinter import *
from mydb import Database
from tkinter import messagebox
from apihandler import SentimentAPI

class NLPApp :

    def __init__(self):

        #create db object
        self.dbo=Database()

        self.apio = SentimentAPI()
        #login ka gui load
        self.root = Tk()
        self.root.title("Natural Language Processing Application")
        # self.root.iconbitmap('resources/favicon.png') #change the image to ico extension
        self.root.geometry("400x600")
        self.root.configure(bg='#34495E')

        self.login_gui()

        self.root.mainloop()


    def login_gui(self):

        heading = Label(self.root,text="NLPApp",bg='#34495E',fg='#ffffff')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana', 24, 'bold'))

        label1= Label(self.root, text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=40)
        self.email_input.pack(pady=(5,10),ipady=5)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)


        login_btn = Button(self.root,text='Login',width=30 , height= 2,command=self.perform_login)
        login_btn.pack(pady=(10,10),ipady=2)

        label3 = Label(self.root, text='Not a Member?')
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root, text='Register Now',command=self.register_gui)
        redirect_btn.pack(pady=(10, 10), ipady=2)

    def register_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='#ffffff')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=40)
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))

        self.email_input = Entry(self.root, width=40)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))

        self.password_input = Entry(self.root, width=40, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.root, text='Register', width=30, height=2,command= self.perform_registration)
        register_btn.pack(pady=(10, 10), ipady=2)

        label3 = Label(self.root, text='Already a Member?')
        label3.pack(pady=(20, 10))

        login_btn = Button(self.root, text='Login Now', command=self.login_again)
        login_btn.pack(pady=(10, 10), ipady=2)



    def login_again(self):
        self.clear()
        self.login_gui()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name, email, password)
        if response:
            messagebox.showinfo('Success', 'Your account has been successfully created. Login now.')
        else:
            messagebox.showerror('Error', 'Email already registered.')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.validate_data(email, password)
        if(response):
            self.load_main()
        else:
            messagebox.showerror('Error', 'Invalid username or password.')


    def load_main(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='#ffffff')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis',width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=30, height=4)
        ner_btn.pack(pady=(10, 10))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=30, height=4,command=self.emotion_gui)
        emotion_btn.pack(pady=(10, 10))

        Logout_btn = Button(self.root, text='Logout', width=30, height=4,command=self.login_again)
        Logout_btn.pack(pady=(10, 10))


    def sentiment_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='#ffffff')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Sentiment Analysis", bg='#34495E', fg='#ffffff')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.text = Entry(self.root, width=40)
        self.text.pack(pady=(5, 10), ipady=5)

        analyze_btn = Button(self.root, text='Analyze Sentiment', width=30, height=4,command=self.analyze_sentiment)
        analyze_btn.pack(pady=(10, 10))

        self.result = Label(self.root, text='',bg='#34495E', fg='#ffffff')
        self.result.pack(pady=(20, 10))
        self.result.configure(font=('verdana', 16))


        Goback_btn = Button(self.root, text='Go Back', width=30, height=4, command=self.load_main)
        Goback_btn.pack(pady=(10, 10))

    def analyze_sentiment(self):
        text = self.text.get()
        result = self.apio.analyze_sentiment(text)

        self.result['text'] = result['sentiment']

        # if "error" in result:
        #     messagebox.showerror("API Error", f"{result['status']} - {result['message']}")
        # else:
        #     polarity = result.get("polarity", "N/A").capitalize()
        #     subjectivity = result.get("subjectivity", "N/A").capitalize()
        #     self.result.config(text=f"Polarity: {polarity}\nSubjectivity: {subjectivity}")


    def emotion_gui(self):
        self.clear()
        heading = Label(self.root, text="NLPApp", bg='#34495E', fg='#ffffff')
        heading.pack(pady=(30, 30))
        heading.configure(font=('verdana', 24, 'bold'))

        heading2 = Label(self.root, text="Emotion Prediction", bg='#34495E', fg='#ffffff')
        heading2.pack(pady=(10, 20))
        heading2.configure(font=('verdana', 20))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(20, 10))

        self.text = Entry(self.root, width=40)
        self.text.pack(pady=(5, 10), ipady=5)

        analyze_btn = Button(self.root, text='Predict Emotion', width=30, height=4, command=self.analyze_emotion)
        analyze_btn.pack(pady=(10, 10))

        self.result = Label(self.root, text='', bg='#34495E', fg='#ffffff')
        self.result.pack(pady=(20, 10))
        self.result.configure(font=('verdana', 16))

        goback_btn = Button(self.root, text='Go Back', width=30, height=4, command=self.load_main)
        goback_btn.pack(pady=(10, 10))

    def analyze_emotion(self):
        text = self.text.get()
        result = self.apio.emotion_analysis(text)

        if not result or not isinstance(result, dict):
            self.result.config(text="Error: No valid response from API.")
            return

        # Get the emotion with the highest probability
        top_emotion = max(result, key=result.get)
        top_score = result[top_emotion]

        # Format display text
        display_text = f"Predicted Emotion: {top_emotion} ({top_score * 100:.2f}%)\n\nEmotion Scores:\n"
        for emotion, score in result.items():
            display_text += f"{emotion}: {score * 100:.2f}%\n"

        self.result.config(text=display_text)
e4t6r5y7382ui9
nlp = NLPApp()