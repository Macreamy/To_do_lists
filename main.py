user_prompt = "Type add, show, edit, complete or exit: "

while True:
    user_action = input(user_prompt)
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo or write back to go to main menu: ") + "\n"
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()
            while todo != "back\n":
                    todos.append(todo)
                    file = open("todo.txt", "w")
                    file.writelines(todos)
                    todo = input("Enter a todo or write back to go to main menu: ") + "\n"
            else:
                print("You have finished adding tasks!")
        case "show" | "display":
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()
            for index, i in enumerate(todos):
                i = i.strip("\n")
                row = f"{index + 1}.{i}"
                print(row)
        case "edit":
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()
            number = int(input("Number of the todo item to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + "\n"
            file = open("todo.txt", "w")
            file.writelines(todos)
            file.close()
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
                open("todo.txt", "w").close()
                print("You have finished all tasks")
        case _:
            print("Hey, unknown command")

print("Bye!")
