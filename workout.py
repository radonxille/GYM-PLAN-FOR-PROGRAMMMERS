from colorama import Fore, init

init(autoreset=True)

def main():
    while True:
        print(Fore.LIGHTRED_EX + '''
        ██████╗ ██╗   ██╗███╗   ██╗    ██████╗ ██╗      █████╗ ███╗   ██╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ██╗  ██╗██╗████████╗
        ██╔════╝ ╚██╗ ██╔╝████╗  ██║    ██╔══██╗██║     ██╔══██╗████╗  ██║██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██║ ██╔╝██║╚══██╔══╝
        ██║  ███╗ ╚████╔╝ ██╔██╗ ██║    ██████╔╝██║     ███████║██╔██╗ ██║███████╗       ██║   ██║   ██║██║   ██║██║     █████╔╝ ██║   ██║   
        ██║   ██║  ╚██╔╝  ██║╚██╗██║    ██╔═══╝ ██║     ██╔══██║██║╚██╗██║╚════██║       ██║   ██║   ██║██║   ██║██║     ██╔═██╗ ██║   ██║   
        ╚██████╔╝   ██║   ██║ ╚████║    ██║     ███████╗██║  ██║██║ ╚████║███████║       ██║   ╚██████╔╝╚██████╔╝███████╗██║  ██╗██║   ██║   
        ╚═════╝    ╚═╝   ╚═╝  ╚═══╝    ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝   
        ''')
        
        print(Fore.LIGHTYELLOW_EX + '''
        1. Bulking Daily Diet (Ethiopian Version)     
        2. Cutting Daily Diet (Ethiopian Version)     
        3. Workout Plan
        4. Exit    
        ''')

        choice = int(input(Fore.LIGHTBLUE_EX + " ENTER YOUR CHOICE SKINNY BITCH 😂: "))

        if choice == 1:
            print(Fore.LIGHTWHITE_EX + '''
            ----------------------------------------------------------------------
            * Breakfast (8:00 AM):
                - Pasta or macaroni (2 cups, cooked)
                - Scrambled eggs (2 large eggs cooked with onions and tomatoes)

            * Mid-Morning Snack (10:30 AM):
                - Roasted peanuts (1 cup)

            * Lunch (1:00 PM):
                - Rice (2 cups, cooked)
                - Tibs (sauteed meat with onions, garlic, and spices)

            * Afternoon Snack (3:30 PM):
                - Banana (2)
                - Avocado (2)

            * Dinner (6:30 PM):
                - Pasta or macaroni (2 cups, cooked)
                - Sega Wat (spicy beef stew made with onions, garlic, and berbere spice blend)
                - Grilled fish (tilapia or similar, 6 oz)

            * Evening Snack (8:30 PM):
                - Peanut butter sandwich (2 slices of bread with 2 tablespoons of peanut butter)

            * Before Bed Snack (10:00 PM):
                - Popcorn (2 cups, air-popped)
            ----------------------------------------------------------------------
            ''')
        elif choice == 2:
            print(Fore.LIGHTRED_EX + "CAUTION: THOSE BULKING AND CUTTING INGREDIENTS ARE THE SAME. JUST MATTERS OF AMOUNTS")
            print(Fore.LIGHTWHITE_EX + '''
            ----------------------------------------------------------------------         
            * Breakfast (8:00 AM)
                - Pasta or Macaroni (1 cup, cooked)
                - Scrambled Eggs (1 large egg cooked with onions and tomatoes)

            * Mid-Morning Snack (10:30 AM)
                - Roasted Peanuts (1/4 cup)

            * Lunch (1:00 PM)
                - Rice (1 cup, cooked)
                - Tibs (sautéed meat with onions, garlic, and spices, reduced portion)

            * Afternoon Snack (3:30 PM)
                - Half a Banana
                - Half an Avocado

            * Dinner (6:30 PM)
                - Pasta or Macaroni (1 cup, cooked)
                - Sega Wat (spicy beef stew made with onions, garlic, and berbere spice blend, reduced portion)
                - Grilled Fish (tilapia or similar, 3 oz)

            * Evening Snack (8:30 PM)
                - Peanut Butter Sandwich (1 slice of bread with 1 tablespoon of peanut butter)

            * Before Bed Snack (10:00 PM)
                - Popcorn (1 cup, air-popped)
            ----------------------------------------------------------------------
            ''')
        elif choice == 3:
            print(Fore.LIGHTWHITE_EX + '''
            ----------------------------------------------------------------------
            * Week 1-5: Workout Schedule

            **Day 1: Chest and Triceps**
            - Bench Press: 4 sets x 8-10 reps
            - Incline Dumbbell Press: 4 sets x 10-12 reps
            - Chest Flyes: 3 sets x 12-15 reps
            - Tricep Dips: 3 sets x 10-12 reps
            - Tricep Pushdowns: 3 sets x 12-15 reps
            - Overhead Tricep Extension: 3 sets x 12-15 reps

            **Day 2: Back and Biceps**
            - Deadlift: 4 sets x 6-8 reps
            - Pull-Ups: 4 sets x 8-10 reps
            - Bent Over Rows: 4 sets x 10-12 reps
            - Face Pulls: 3 sets x 12-15 reps
            - Barbell Curls: 3 sets x 10-12 reps
            - Hammer Curls: 3 sets x 12-15 reps

            **Day 3: Rest**

            **Day 4: Legs and Abs**
            - Squats: 4 sets x 8-10 reps
            - Leg Press: 4 sets x 10-12 reps
            - Romanian Deadlifts: 4 sets x 10-12 reps
            - Leg Curls: 3 sets x 12-15 reps
            - Calf Raises: 4 sets x 15-20 reps
            - Plank: 3 sets x 1 minute
            - Russian Twists: 3 sets x 20 reps

            **Day 5: Shoulders and Traps**
            - Overhead Press: 4 sets x 8-10 reps
            - Lateral Raises: 4 sets x 12-15 reps
            - Front Raises: 3 sets x 12-15 reps
            - Rear Delt Flyes: 3 sets x 12-15 reps
            - Shrugs: 4 sets x 10-12 reps

            **Day 6: Full Body**
            - Power Clean: 4 sets x 6-8 reps
            - Pull-Ups: 4 sets x 8-10 reps
            - Squats: 4 sets x 8-10 reps
            - Bench Press: 4 sets x 8-10 reps
            - Plank: 3 sets x 1 minute

            **Day 7: Rest**

            * Tips for Success
            - **Progressive Overload:** Gradually increase the weights you lift each week to continue building muscle.
            - **Rest:** Ensure you get adequate rest and recovery, especially on rest days.
            - **Nutrition:** Follow your bulking diet plan closely to ensure you’re consuming enough calories and protein for muscle growth.
            - **Hydration:** Drink plenty of water throughout the day.
            - **Sleep:** Aim for 7-9 hours of quality sleep each night to support recovery and muscle growth.
            ----------------------------------------------------------------------
            ''')
        elif choice == 4:
            print(Fore.LIGHTWHITE_EX + "Exiting the program. Goodbye!")
            break
        else:
            print(Fore.LIGHTRED_EX + "Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
