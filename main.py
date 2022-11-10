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
            for index, i in enumerate(todos):
                i = i.title()
                row = f"{index + 1}.{i}"
                print(row)
        case "edit":
            number = int(input("Number of the todo item to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo
            print(new_todo)
        case "exit":
            break
        case "complete":
            number = int(input("Number of the todo item to complete: "))
            completed = todos.pop(number - 1)
            print("You have completed", completed)
        case _:
            print("Hey, unknown command")

print("Bye!")
