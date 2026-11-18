pub trait Describe {
    fn describe(&self) -> &str;
}

pub struct Label<'a> {
    pub text: &'a str,
    pub visible: bool,
}

impl Describe for Label<'_> {
    fn describe(&self) -> &str {
        self.text
    }
}

macro_rules! label_length {
    ($label:expr) => {
        $label.text.len()
    };
}

pub fn visible_length(label: &Label<'_>) -> usize {
    if !label.visible {
        return 0;
    }

    label_length!(label)
}
