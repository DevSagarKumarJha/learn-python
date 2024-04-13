import sqlite3

conn = sqlite3.connect("youtube_videos.db")

cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS videos (
               video_id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
  )'''
)


def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES(?, ?)", (name, time))
    conn.commit()


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ? , time = ? WHERE video_id = ?", (new_name, new_time, video_id))
    conn.commit()


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE video_id = ?", (video_id,))


def main():
    while True:
        print("\n Youtube Manager app with db | choose a option")
        print("1. List videos")
        print("2. Add  videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit the app")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_videos()
        elif choice == "2":
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            add_video(name, time)
        elif choice == "3":
            video_id = input("Enter your video video_id to update: ")
            name = input("Enter your video name: ")
            time = input("Enter your video time: ")
            update_video(video_id, name, time)
        elif choice == "4":
            video_id = input("Enter your video video_id to delete: ")
            delete_video(video_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice !")

    conn.close()


if __name__ == "__main__":
    main()
