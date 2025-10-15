import tkinter as tk
import random
from tkinter import font

# Comprehensive list of Specialist Tasks (Blue Box) - tasks that only normal specialists get
specialist_tasks = [
    {
        "name": "Sales Confirmation",
        "steps": [
            "1. Use computer to email client",
            "2. Print sales confirmation document",
            "3. Pick up document from copier room",
            "4. Sign the document",
            "5. Drop off at designated location"
        ]
    },
    {
        "name": "Report Relay",
        "steps": [
            "1. Find the sales report or customer survey",
            "2. Sign the document at your desk",
            "3. Pin the report to the bulletin board"
        ]
    },
    {
        "name": "Ream Reload (Paper Reload)",
        "steps": [
            "1. Go to the copier room",
            "2. Pick up paper ream from supplies",
            "3. Restock the printer with paper"
        ]
    },
    {
        "name": "Operation Shred",
        "steps": [
            "1. Find documents that need shredding",
            "2. Go to the copier room",
            "3. Use the shredder to destroy documents"
        ]
    },
    {
        "name": "Cats Also Need to Eat!",
        "steps": [
            "1. Pick up cat food from the cupboard",
            "2. Go to the room with the office cats",
            "3. Feed the cats by interacting with them"
        ]
    },
    {
        "name": "Warehouse Wishlist",
        "steps": [
            "1. Take the elevator to the warehouse",
            "2. Create inventory list of needed items",
            "3. Return and submit the list"
        ]
    },
    {
        "name": "Duplicate Dispatch",
        "steps": [
            "1. Retrieve the file from designated location",
            "2. Go to copier room and make a copy",
            "3. Place copy in a random desk bin"
        ]
    },
    {
        "name": "Wipe Assistance",
        "steps": [
            "1. Find cleaning supplies in supply room",
            "2. Locate areas that need cleaning",
            "3. Clean designated surfaces"
        ]
    },
    {
        "name": "Document Dispatch (Doc Dispatch)",
        "steps": [
            "1. Check your email for document request",
            "2. Locate the file for faxing",
            "3. Go to copier room and fax the document"
        ]
    },
    {
        "name": "OCD (Organize Cabinet Drawers)",
        "steps": [
            "1. Find the filing cabinet (check your map)",
            "2. Open the cabinet drawers",
            "3. Organize files into proper order"
        ]
    },
    {
        "name": "Where's the Janitor?",
        "steps": [
            "1. Search the office floors for janitor",
            "2. Check common areas like bathroom and kitchen",
            "3. Report janitor location to manager"
        ]
    },
    {
        "name": "Fresh Firmware",
        "steps": [
            "1. Go to the server room",
            "2. Use computer to download firmware update",
            "3. Install update and restart server"
        ]
    },
    {
        "name": "Back to Basics",
        "steps": [
            "1. Review basic office protocols",
            "2. Check supply inventory levels",
            "3. Report any deficiencies to manager"
        ]
    }
]

# Slacking Tasks (Red Box) - tasks both specialists and slackers can get
slacking_tasks = [
    {
        "name": "Caffeine Boost",
        "steps": [
            "1. Grab your mug from your desk",
            "2. Go to the kitchen",
            "3. Fill your mug with coffee and drink it"
        ]
    },
    {
        "name": "The Mines Won't Sweep Themselves!",
        "steps": [
            "1. Use computer at your desk",
            "2. Open Minesweeper game",
            "3. Play until you complete a game"
        ]
    },
    {
        "name": "I'm a Cat Person!",
        "steps": [
            "1. Go to the room with office cats",
            "2. Interact with the cats",
            "3. Pet them for designated time"
        ]
    },
    {
        "name": "Call of Nature",
        "steps": [
            "1. Go to the bathroom/toilet area",
            "2. Use the facilities",
            "3. Return to your desk"
        ]
    },
    {
        "name": "Refreshment Recess",
        "steps": [
            "1. Go to the kitchen area",
            "2. Use the vending machine",
            "3. Grab a snack and consume it"
        ]
    }
]

class TaskGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dale & Dawson Task Generator - Slacker Edition")
        self.root.geometry("700x750")
        self.root.resizable(False, False)
        root.iconbitmap("icon.png")

        # Set background color to match office theme
        self.root.configure(bg='#f0f0f0')

        # Create custom fonts
        title_font = font.Font(family="Arial", size=16, weight="bold")
        task_title_font = font.Font(family="Arial", size=12, weight="bold")
        step_font = font.Font(family="Arial", size=10)

        # Title label
        title_label = tk.Label(
            root, 
            text="Dale & Dawson Stationery Supplies\nSpecialist Task List", 
            font=title_font,
            bg='#2c5aa0',
            fg='white',
            pady=15
        )
        title_label.pack(fill='x')

        # Subtitle
        subtitle_label = tk.Label(
            root,
            text="Your current assigned tasks:",
            font=("Arial", 10, "italic"),
            bg='#f0f0f0',
            fg='#333333'
        )
        subtitle_label.pack(pady=(10, 5))

        # Legend for task types
        legend_frame = tk.Frame(root, bg='#f0f0f0')
        legend_frame.pack(pady=5)
        
        specialist_legend = tk.Label(
            legend_frame,
            text="● Specialist Task",
            font=("Arial", 8),
            bg='#f0f0f0',
            fg='#1976d2'
        )
        specialist_legend.pack(side='left', padx=10)
        
        slacker_legend = tk.Label(
            legend_frame,
            text="● Slacker Task",
            font=("Arial", 8),
            bg='#f0f0f0',
            fg='#d32f2f'
        )
        slacker_legend.pack(side='left', padx=10)

        # Frame for tasks
        self.tasks_frame = tk.Frame(root, bg='#f0f0f0')
        self.tasks_frame.pack(pady=10, padx=20, fill='both', expand=True)

        # Store task labels
        self.task_labels = []

        # Generate button
        generate_btn = tk.Button(
            root,
            text="Generate New Tasks",
            command=self.generate_tasks,
            font=("Arial", 12, "bold"),
            bg='#4CAF50',
            fg='white',
            activebackground='#45a049',
            pady=10,
            cursor='hand2'
        )
        generate_btn.pack(pady=15)

        # Generate initial tasks
        self.generate_tasks()

    def is_slacker_task(self, task_name):
        """Check if a task is a slacker task"""
        slacker_names = [task['name'] for task in slacking_tasks]
        return task_name in slacker_names

    def generate_tasks(self):
        # Clear previous tasks
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        # Decide randomly whether to include 0 or 1 slacker tasks
        include_slacker = random.choice([True, False])
        
        selected_tasks = []
        
        if include_slacker:
            # Add 1 slacker task and 2 specialist tasks
            slacker_task = random.choice(slacking_tasks)
            specialist_tasks_selected = random.sample(specialist_tasks, 2)
            selected_tasks = [slacker_task] + specialist_tasks_selected
        else:
            # Add 3 specialist tasks
            selected_tasks = random.sample(specialist_tasks, 3)
        
        # Shuffle the order so the slacker task isn't always first
        random.shuffle(selected_tasks)

        # Display each task
        for i, task in enumerate(selected_tasks, 1):
            # Task container frame
            task_container = tk.Frame(
                self.tasks_frame,
                bg='white',
                relief='raised',
                borderwidth=2
            )
            task_container.pack(fill='x', pady=8)

            # Determine if this is a slacker task
            is_slacker = self.is_slacker_task(task['name'])
            
            # Set colors based on task type
            if is_slacker:
                header_bg = '#ffebee'  # Light red background
                header_fg = '#d32f2f'  # Dark red text
                border_color = '#d32f2f'
            else:
                header_bg = '#e3f2fd'  # Light blue background
                header_fg = '#1976d2'  # Dark blue text
                border_color = '#1976d2'

            # Add colored border to indicate task type
            task_container.configure(highlightbackground=border_color, highlightthickness=1)

            # Task number and name
            task_header = tk.Label(
                task_container,
                text=f"Task {i}: {task['name']}",
                font=("Arial", 11, "bold"),
                bg=header_bg,
                fg=header_fg,
                anchor='w',
                padx=10,
                pady=5
            )
            task_header.pack(fill='x')

            # Add slacker indicator for slacker tasks
            if is_slacker:
                slacker_indicator = tk.Label(
                    task_header,
                    text="(Slacker Task)",
                    font=("Arial", 8, "italic"),
                    bg=header_bg,
                    fg=header_fg,
                    anchor='e'
                )
                slacker_indicator.pack(side='right', padx=5)

            # Task steps
            steps_frame = tk.Frame(task_container, bg='white')
            steps_frame.pack(fill='x', padx=15, pady=8)

            for step in task['steps']:
                step_label = tk.Label(
                    steps_frame,
                    text=step,
                    font=("Arial", 9),
                    bg='white',
                    fg='#333333',
                    anchor='w',
                    justify='left'
                )
                step_label.pack(anchor='w', pady=2)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskGeneratorApp(root)
    root.mainloop()