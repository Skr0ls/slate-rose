protocol Describable {
    var description: String { get }
}

enum ReviewError: Error {
    case invalid
}

struct Box<Value> {
    var value: Value
}

typealias Count = Int

struct Item: Describable {
    let name: String
    var count: Count
    var enabled: Bool
    var weight: Float
    var optionalCount: Int?
    var explicitOptional: Optional<Int>
    var history: Array<Int>
    var boxed: Box<Int>

    var description: String { name }

    func checkedCount() throws -> Int {
        if !enabled {
            throw ReviewError.invalid
        }
        return count
    }
}

func makeItem() -> Item {
    let count: Int = Int(3)
    let name: String = String("Slate")
    let enabled: Bool = Bool(true)
    let weight: Float = Float(1.5)
    return Item(name: name, count: count, enabled: enabled, weight: weight,
                optionalCount: nil, explicitOptional: Optional<Int>.some(count),
                history: Array<Int>(), boxed: Box<Int>(value: count))
}

func describe(_ value: any Describable) -> String {
    return value.description
}

func makeDescribable() -> some Describable {
    return makeItem()
}
