// swift-tools-version:4.2
import PackageDescription

let package = Package(
    name: "MellonApp",
    products: [
        .library(name: "MellonApp", targets: ["App"]),
    ],
    dependencies: [
        // 💧 A server-side Swift web framework.
        .package(url: "https://github.com/vapor/vapor.git", from: "3.0.0"),

        // 🔵 Swift ORM (queries, models, relations, etc) built on SQLite 3.
//        .package(url: "https://github.com/vapor/fluent-sqlite.git", from: "3.0.0"),
        .package(path: "../MellonCommon"),
        .package(path: "../MellonCore"),
        .package(path: "../MellonSlackModule"),
//        .package(path: "../MellonDiscordModule"),
    ],
    targets: [
        .target(name: "App", dependencies: ["MellonCommon", "MellonCore", "MellonSlackModule", "Vapor"]),
        .target(name: "Run", dependencies: ["App"]),
        .testTarget(name: "AppTests", dependencies: ["App"]),
    ]
)
