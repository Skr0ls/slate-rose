package showcase

const limit int = 3

type Person struct {
	Name   string
	Active bool
}

func FirstActive[T any](people []T, active func(T) bool) (T, bool) {
	for _, person := range people {
		if active(person) {
			return person, true
		}
	}
	var zero T
	return zero, false
}

func IsActive(person Person) bool {
	return person.Active && len(person.Name) > limit
}
