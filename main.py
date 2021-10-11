from tkinter import *
from tkinter import messagebox
from random import shuffle

my_list = ['pay', 'dimension', 'cottage', 'grand', 'force', 'extinct', 'offset', 'hobby', 'monster', 'pasture', 'burst',
           'burial', 'exposure', 'defendant', 'keep', 'grass', 'shed', 'convulsion', 'plastic', 'explode', 'form',
           'advocate', 'overeat', 'card', 'joke', 'frozen', 'betray', 'concession', 'category', 'pollution',
           'experiment', 'contrast', 'glow', 'banner', 'writer', 'plaintiff', 'roll', 'reproduce', 'triangle',
           'presidency', 'rare', 'electron', 'winter', 'royalty', 'sentiment', 'urine', 'cathedral', 'failure',
           'tragedy', 'stain', 'prison', 'last', 'runner', 'shelter', 'initiative', 'truth', 'addicted', 'fur',
           'sight', 'initial', 'fill', 'flood', 'perfect', 'half', 'coffin', 'reputation', 'budge', 'slow', 'dinner',
           'overlook', 'feel', 'demand', 'scandal', 'remember', 'stunning', 'stage', 'promise', 'disorder', 'fireplace',
           'clarify', 'speculate', 'tasty', 'patch', 'outer', 'sister', 'zero', 'approach', 'core', 'stool',
           'investigation', 'announcement', 'understanding', 'staff', 'extort', 'child', 'pierce', 'patrol', 'pocket',
           'rescue', 'strange', 'brain', 'content', 'have', 'initiative', 'recommend', 'presidential', 'imposter',
           'suburb', 'kidnap', 'tycoon', 'god', 'lost', 'iron', 'allow', 'neighborhood', 'omission', 'number', 'abuse',
           'fate', 'deprivation', 'witch', 'climb', 'prevalence', 'consensus', 'galaxy', 'west', 'couple', 'sea',
           'siege', 'guerrilla', 'lose', 'winner', 'tray', 'road', 'wrong', 'report', 'convince', 'ivory', 'wait',
           'publish', 'crop', 'frame', 'comfortable', 'garbage', 'partnership', 'toll', 'humor', 'nerve', 'technology',
           'the', 'of', 'and', 'to', 'a', 'in', 'is', 'you', 'are', 'for', 'that', 'or', 'it', 'as', 'be', 'on', 'your',
           'with', 'can', 'have', 'this', 'an', 'by', 'not', 'but', 'at', 'from', 'I', 'they', 'more', 'will', 'if',
           'some', 'there', 'what', 'about', 'which', 'when', 'one', 'their', 'all', 'also', 'how', 'many', 'do', 'has',
           'most', 'people', 'other', 'time', 'so', 'was', 'we', 'these', 'may', 'like', 'use', 'into', 'than', 'up',
           'out', 'who', 'them', 'make', 'because', 'such', 'through', 'get', 'work', 'even', 'different', 'its', 'no',
           'our', 'new', 'film', 'just', 'only', 'see', 'used', 'good', 'water', 'been', 'need', 'should', 'very',
           'any', 'history', 'often', 'way', 'well', 'art', 'know', 'were', 'then', 'my', 'first', 'would', 'money',
           'each', 'over', 'world', 'information', 'map', 'find', 'where', 'much', 'take', 'two', 'want', 'important',
           'family', 'those', 'example', 'while', 'he', 'look', 'government', 'before', 'help', 'between', 'go', 'own',
           'however', 'business', 'us', 'great', 'his', 'being', 'another', 'health', 'same', 'study', 'why', 'few',
           'game', 'might', 'think', 'free', 'too', 'had', 'hi', 'right', 'still', 'system', 'after', 'computer',
           'best', 'must', 'her', 'life', 'since', 'could', 'does', 'now', 'during', 'learn', 'around', 'usually',
           'form', 'meat', 'air', 'day', 'place', 'become', 'number', 'public', 'read', 'keep', 'part', 'start', 'year',
           'every', 'field', 'large', 'once', 'available', 'down', 'give', 'fish', 'human', 'both', 'local', 'sure',
           'something', 'without', 'come', 'me', 'back', 'better', 'general', 'process', 'she', 'heat', 'thanks',
           'specific', 'enough', 'long', 'lot', 'hand', 'popular', 'small', 'though', 'experience', 'include', 'job',
           'music', 'person', 'really', 'although', 'thank', 'book', 'early', 'reading', 'end', 'method', 'never',
           'less', 'play', 'able', 'data', 'feel', 'high', 'off', 'point', 'type', 'whether', 'food', 'understanding',
           'here', 'home', 'certain', 'economy', 'little', 'theory', 'tonight', 'law', 'put', 'under', 'value',
           'always', 'body', 'common', 'market', 'set', 'bird', 'guide', 'provide', 'change', 'interest', 'literature',
           'sometimes', 'problem', 'say', 'next', 'create', 'simple', 'software', 'state', 'together', 'control',
           'knowledge', 'power', 'radio', 'ability', 'basic', 'course', 'economics', 'hard', 'add', 'company', 'known',
           'love', 'past', 'price', 'size', 'away', 'big', 'internet', 'possible', 'television', 'three', 'understand',
           'various', 'yourself', 'card', 'difficult', 'including', 'list', 'mind', 'particular', 'real', 'science',
           'trade', 'consider', 'either', 'library', 'likely', 'nature', 'fact', 'line', 'product', 'care', 'group',
           'idea', 'risk', 'several', 'someone', 'temperature', 'united', 'word', 'fat', 'force', 'key', 'light',
           'simply', 'today', 'training', 'until', 'major', 'name', 'personal', 'school', 'top', 'current', 'generally']


level_of_game = []
answer = []
wrong = []
timer = None


def radio_used():
    global level_of_game
    user_level = radio_state.get()
    if user_level == 1:
        for lvl in my_list:
            if len(lvl) < 6:
                level_of_game.append(lvl)

    elif user_level == 2:
        for lvl in my_list:
            if len(lvl) < 8:
                level_of_game.append(lvl)
    elif user_level == 3:
        level_of_game = my_list
    shuffle(level_of_game)


def start_timer():
    text = Label(text=level_of_game[:50], pady=20, padx=30, wraplength=400, bg='lightyellow', fg="royalblue", font=("Arial", 15, "bold"))
    text.grid(row=2, columnspan=3, rowspan=5, pady=20)
    typing.grid(row=7, columnspan=3, pady=20)
    count_down(60)


def count_down(count):
    count_sec = count
    if count_sec == 0:
        done.grid(row=8, column=1)
        window.config(cursor="none")
        typing.config(state=DISABLED)
        user_input = typing.get("1.0", END).split()
        for inp in user_input:
            if inp in level_of_game:
                answer.append(inp)
            else:
                wrong.append(inp)
        message = f'You have written {len(answer)} words in a minute!'
        messagebox.showinfo(title='Results!', message=message)
        if len(wrong) != 0:
            messagebox.showerror(title='Errors', message=f'You have inserted {wrong} incorrectly!')
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"00:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)


####################################################
window = Tk()
window.title('Type Tester')
window.config(padx=30, pady=30, bg='white')

canvas = Canvas(width=130, height=130, bg='white', highlightthickness=0)
photo = PhotoImage(file='rasm.png')
canvas.create_image(64, 64, image=photo)
timer_text = canvas.create_text(64, 75, text="00:00", fill="black", font=("Arial", 18, "bold"))
canvas.grid(row=0, column=1)

level = Label(text="Choose your level", bg='white', font=("Arial", 12, "bold"))
level.grid(row=2, column=1, padx=30, pady=30)


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Easy", value=1, variable=radio_state, command=radio_used, bg='white', font=("Arial", 15, "bold"))
radiobutton2 = Radiobutton(text="Medium", value=2, variable=radio_state, command=radio_used, bg='white', font=("Arial", 15, "bold"))
radiobutton3 = Radiobutton(text="Hard", value=3, variable=radio_state, command=radio_used, bg='white', font=("Arial", 15, "bold"))
radiobutton1.grid(padx=10, pady=10, row=3, column=0)
radiobutton2.grid(padx=10, pady=10, row=3, column=1)
radiobutton3.grid(padx=10, pady=10, row=3, column=2)

start = Button(text='Start', command=start_timer, bg='white', padx=2, pady=1, font=("Arial", 15, "bold"))
start.grid(padx=10, pady=10, row=4, column=1)


typing = Text(width=42, height=5, fg='green', font=("Arial", 15, "bold"))
typing.focus()

done = Label(text='Well done 👏🏼', bg='white', fg='red', font=("Times", 20, "bold"))

window.mainloop()
