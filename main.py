user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo or write back to go to main menu: ") + "\n"
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            while todo != "back\n":
                    todos.append(todo)
                    with open("todo.txt", "w") as file:
                        file.writelines(todos)
                    todo = input("Enter a todo or write back to go to main menu: ") + "\n"
            else:
                print("You have finished adding tasks!")
        case "show" | "display":
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            for index, i in enumerate(todos):
                i = i.strip("\n")
                row = f"{index + 1}.{i}"
                print(row)
        case "edit":
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            number = int(input("Number of the todo item to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            with open("todo.txt", "w") as file:
                todos = file.writelines(new_todo)
            print(new_todo)
        case "exit":
            break
        case "complete":
            user_text = input("Number of the todo item to complete it or write complete all to finish all remaining tasks: ")
            number = user_text
            while number != "complete all":
                number = int(number)
                completed = todos.pop(number - 1)
                print("You have completed", completed)
            else:
                completed = ""
                with open("todo.txt", "w") as file:
                    todos = file.writelines(completed)
                print("You have finished all tasks")
        case _:
            print("Hey, unknown command")

print("Bye!")
