import json
from datetime import datetime


class Relapse:
    def __init__(self, name, age_when_we_fell_in_love, favorite_color, current_age):
        self.name = name
        self.age_when_we_fell_in_love = age_when_we_fell_in_love
        self.current_age = current_age
        self.favorite_color = favorite_color
        self.memories = []  # To store cherished memories
        self.milestones = []  # To store relationship milestones
        self.special_dates = []  # To store special dates and messages
        self.mood = "neutral"  # Default mood
        self.quotes_songs = []  # To store favorite quotes or songs
        self.letters = []  # To store unsent letters

        # Load data from file
        self.load_data()

    def introduce_person(self):
        print(f"Her name is {self.name}. We were {self.age_when_we_fell_in_love} when we fell in love. I still remember her favorite color, {self.favorite_color}.")
    
    def about_her(self):
        print(f"She loves Tulips, the color {self.favorite_color}, and the smell of rain.")
    
    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.memories = data.get("memories", [])
                self.milestones = data.get("milestones", [])
                self.special_dates = data.get("special_dates", [])
                self.mood = data.get("mood", "neutral")
                self.quotes_songs = data.get("quotes_songs", [])
                self.letters = data.get("letters", [])
        except FileNotFoundError:
            print("No previous data found. Starting fresh.")

    def save_data(self):
        data = {
            "memories": self.memories,
            "milestones": self.milestones,
            "special_dates": self.special_dates,
            "mood": self.mood,
            "quotes_songs": self.quotes_songs,
            "letters": self.letters
        }
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully.")

    # Feature 1: Memory Keeper
    def add_memory(self, memory, media_link=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        memory_data = {"memory": memory, "timestamp": timestamp, "media": media_link}
        self.memories.append(memory_data)
        print(f"Memory added: '{memory}' at {timestamp}.")
        if media_link:
            print(f"Associated Media: {media_link}")
        self.save_data()

    def list_memories(self):
        if self.memories:
            print("Cherished Memories:")
            for i, memory in enumerate(self.memories, start=1):
                print(f"{i}. {memory['memory']} (Added on: {memory['timestamp']})")
                if memory['media']:
                    print(f"   Media: {memory['media']}")
        else:
            print("No memories recorded yet.")

    def delete_memory(self, index):
        if 0 <= index < len(self.memories):
            deleted_memory = self.memories.pop(index)
            print(f"Memory deleted: '{deleted_memory['memory']}'")
            self.save_data()
        else:
            print("Invalid memory index.")

    # Feature 2: Milestones
    def add_milestone(self, milestone, media_link=None):
        milestone_data = {"milestone": milestone, "media": media_link}
        self.milestones.append(milestone_data)
        print(f"Milestone added: {milestone}")
        if media_link:
            print(f"Associated Media: {media_link}")
        self.save_data()

    def list_milestones(self):
        if self.milestones:
            print("Relationship Milestones:")
            for i, milestone in enumerate(self.milestones, start=1):
                print(f"{i}. {milestone['milestone']}")
                if milestone['media']:
                    print(f"   Media: {milestone['media']}")
        else:
            print("No milestones recorded yet.")

    def delete_milestone(self, index):
        if 0 <= index < len(self.milestones):
            deleted_milestone = self.milestones.pop(index)
            print(f"Milestone deleted: '{deleted_milestone['milestone']}'")
            self.save_data()
        else:
            print("Invalid milestone index.")

    # Feature 3: Special Dates
    def add_special_date(self, date, message):
        special_date_data = {"date": date, "message": message}
        self.special_dates.append(special_date_data)
        print(f"Special date added: {date} with message: '{message}'")
        self.save_data()

    def check_special_dates(self):
        today = datetime.now().strftime("%Y-%m-%d")
        for special_date in self.special_dates:
            if special_date['date'] == today:
                print(f"Today's Special Date: {special_date['date']} - {special_date['message']}")

    # Feature 4: Mood Simulation
    def set_mood(self, mood):
        self.mood = mood
        print(f"Your mood has been set to: {mood}")
        self.save_data()

    def display_mood(self):
        responses = {
            "happy": f"{self.name} is glad to see you smiling. Cherish the good times.",
            "sad": f"{self.name} says it's okay to cry. Healing takes time.",
            "neutral": f"{self.name} understands. Sometimes it's just another day.",
            "angry": f"{self.name} reminds you to breathe. Letting go is part of the process."
        }
        print(responses.get(self.mood, "Mood not recognized."))

    # Feature 5: Quotes and Songs
    def add_quote_song(self, quote_song):
        self.quotes_songs.append(quote_song)
        print(f"Quote/Song added: {quote_song}")
        self.save_data()

    def list_quotes_songs(self):
        if self.quotes_songs:
            print("Favorite Quotes/Songs:")
            for i, quote_song in enumerate(self.quotes_songs, start=1):
                print(f"{i}. {quote_song}")
        else:
            print("No quotes or songs recorded yet.")

    def delete_quote_song(self, index):
        if 0 <= index < len(self.quotes_songs):
            deleted_quote_song = self.quotes_songs.pop(index)
            print(f"Quote/Song deleted: '{deleted_quote_song}'")
            self.save_data()
        else:
            print("Invalid index.")

    # Feature 6: Letters
    def write_letter(self, letter):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        letter_data = {"letter": letter, "timestamp": timestamp}
        self.letters.append(letter_data)
        print(f"Letter written: '{letter}' at {timestamp}.")
        self.save_data()

    def list_letters(self):
        if self.letters:
            print("Unsent Letters:")
            for i, letter in enumerate(self.letters, start=1):
                print(f"{i}. {letter['letter']} (Written on: {letter['timestamp']})")
        else:
            print("No letters written yet.")

    def delete_letter(self, index):
        if 0 <= index < len(self.letters):
            deleted_letter = self.letters.pop(index)
            print(f"Letter deleted: '{deleted_letter['letter']}'")
            self.save_data()
        else:
            print("Invalid index.")


# Example usage
if __name__ == "__main__":
    p1 = Relapse("Name", 20, "Purple", 20)

    while True:
        print("\n=== Menu ===")
        print("1. Introduce Person")
        print("2. Know More About Rhei")
        print("3. Add Memory")
        print("4. List Memories")
        print("5. Delete Memory")
        print("6. Add Milestone")
        print("7. List Milestones")
        print("8. Delete Milestone")
        print("9. Add Special Date")
        print("10. Check Special Dates")
        print("11. Set Mood")
        print("12. Display Mood")
        print("13. Add Quote/Song")
        print("14. List Quotes/Songs")
        print("15. Delete Quote/Song")
        print("16. Write Letter")
        print("17. List Letters")
        print("18. Delete Letter")
        print("19. Exit")

        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            p1.introduce_person()
        elif choice == "2":
            print(p1.about_her())
        elif choice == "3":
            memory = input("Enter a cherished memory: ").strip()
            media_link = input("Enter a media link (optional): ").strip() or None
            p1.add_memory(memory, media_link)
        elif choice == "4":
            p1.list_memories()
        elif choice == "5":
            index = int(input("Enter the memory index to delete: ")) - 1
            p1.delete_memory(index)
        elif choice == "6":
            milestone = input("Enter a relationship milestone: ").strip()
            media_link = input("Enter a media link (optional): ").strip() or None
            p1.add_milestone(milestone, media_link)
        elif choice == "7":
            p1.list_milestones()
        elif choice == "8":
            index = int(input("Enter the milestone index to delete: ")) - 1
            p1.delete_milestone(index)
        elif choice == "9":
            date = input("Enter the special date (YYYY-MM-DD): ").strip()
            message = input("Enter a message for this special date: ").strip()
            p1.add_special_date(date, message)
        elif choice == "10":
            p1.check_special_dates()
        elif choice == "11":
            mood = input("Enter your mood (happy, sad, neutral, angry): ").strip().lower()
            p1.set_mood(mood)
        elif choice == "12":
            p1.display_mood()
        elif choice == "13":
            quote_song = input("Enter a favorite quote or song: ").strip()
            p1.add_quote_song(quote_song)
        elif choice == "14":
            p1.list_quotes_songs()
        elif choice == "15":
            index = int(input("Enter the quote/song index to delete: ")) - 1
            p1.delete_quote_song(index)
        elif choice == "16":
            letter = input("Write an unsent letter to Rhei: ").strip()
            p1.write_letter(letter)
        elif choice == "17":
            p1.list_letters()
        elif choice == "18":
            index = int(input("Enter the letter index to delete: ")) - 1
            p1.delete_letter(index)
        elif choice == "19":
            print("Goodbye. Take care!")
            break
        else:
            print("Invalid choice. Please try again.")
