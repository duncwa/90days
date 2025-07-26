import UIKit
import SwiftUI

var greeting = "Hello, playground"
var name = "Duncan"
var age = 65
var language: String? = nil
language = String("Swift")
var favoriteNumber: Int? = nil
favoriteNumber = Int("42")
if let favoriteLanguage = language {
    greeting = "Hello \(name).  Your age is \(age) and your favorite language is \(favoriteLanguage)."
    print(greeting)
} else {
    print("no favorite language entered.")
}

