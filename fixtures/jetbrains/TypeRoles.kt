package preview

typealias Label = String

class TypeRoles {
    var count: Int = 0
        get() = field
    val title: String = "Slate Rose"
    val enabled: Boolean = true
    val scale: Float = 1.5f
    val optionalTitle: String? = null
    val counts: List<Int> = listOf(1, 2)
    val aliasTitle: Label = title

    fun describe(inputCount: Int, inputTitle: String, isEnabled: Boolean, inputScale: Float): String {
        val nextCount: Int = inputCount + count
        val displayTitle: String = inputTitle
        val active: Boolean = isEnabled
        val adjustedScale: Float = inputScale * scale
        if (!active) return displayTitle
        return when (nextCount) {
            0 -> throw IllegalArgumentException("Count must be positive")
            else -> "$displayTitle: $adjustedScale"
        }
    }

    fun acknowledge(): Unit {
        val completion: Unit = Unit
        return completion
    }
}
