import MellonSlackModule
import Vapor

/// Register your application's routes here.
public func routes(_ router: Router) throws {
    // Basic "It works" example
    router.get { _ in
        "It works!"
    }

    // Basic "Hello, world!" example
    router.get("status") { _ in
        "Hello, world!"
    }

    let slackController = SlackController()
    try router.register(collection: slackController)

    // Example of configuring a controller
    // let todoController = TodoController()
    // router.get("todos", use: todoController.index)
    // router.post("todos", use: todoController.create)
    // router.delete("todos", Todo.parameter, use: todoController.delete)
}
