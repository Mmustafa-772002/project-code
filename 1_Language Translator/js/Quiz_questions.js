// creating an array and passing the number, questions, options, and answers
let questions = [

  {
    numb: 1,
    question: "What is a verb?",
    answer: "An action or state of being",
    options: [
      "A person, place, or thing",
      "An action or state of being",
      "A descriptive word",
      "None of the above",
    ],
  },
  {
    numb: 2,
    question: "What is the plural form of 'child'?",
    answer: "children",
    options: ["childs", "childen", "child's", "children"],
  },
  {
    numb: 3,
    question: "What is the past tense of the verb 'to go'?",
    answer: "went",
    options: ["goes", "gone", "going", "went"],
  },
  {
    numb: 4,
    question: "Which of the following is a preposition?",
    answer: "with",
    options: ["sing", "happily", "with", "jumped"],
  },
  {
    numb: 5,
    question: "What is an adjective?",
    answer: "A word that describes a noun or pronoun",
    options: [
      "A person, place, or thing",
      "A word that describes a noun or pronoun",
      "A verb",
      "None of the above",
    ],
  },
  {
    numb: 6,
    question: "Which of these words is a pronoun?",
    answer: "she",
    options: ["jump", "quickly", "she", "friendly"],
  },
  {
    numb: 7,
    question: "What is the correct plural form of 'tomato'?",
    answer: "tomatoes",
    options: ["tomatos", "tomaties", "tomatoe", "tomatoes"],
  },
  {
    numb: 8,
    question: "What is the comparative form of the adjective 'big'?",
    answer: "bigger",
    options: ["big", "bigger", "bigly", "biggest"],
  },
  {
    numb: 9,
    question: "Which sentence is in the passive voice?",
    answer: "The cake was eaten by her.",
    options: [
      "She ate the cake.",
      "The cake was eaten by her.",
      "They will bake cookies.",
      "He is reading a book.",
    ],
  },
  {
    numb: 10,
    question: "What is a conjunction?",
    answer: "A word that joins words, phrases, or clauses",
    options: [
      "A type of punctuation mark",
      "A word that joins words, phrases, or clauses",
      "A type of verb",
      "A proper noun",
    ],
  },
  {
    numb: 11,
    question: "What is the superlative form of the adjective 'happy'?",
    answer: "happiest",
    options: ["happy", "happier", "happilier", "happiest"],
  },
  {
    numb: 12,
    question: "Identify the adverb in the sentence: 'She sings beautifully.'",
    answer: "beautifully",
    options: ["She", "sings", "beautifully", "None of the above"],
  },
  {
    numb: 13,
    question:
      "Which word is a noun in the sentence: 'The cat chased the mouse'?",
    answer: "cat",
    options: ["cat", "chased", "the", "mouse"],
  },
  {
    numb: 14,
    question: "What is the plural form of 'deer'?",
    answer: "deer",
    options: ["deers", "deer", "deeries", "None of the above"],
  },
  {
    numb: 15,
    question: "What is the correct past tense of 'run'?",
    answer: "ran",
    options: ["runned", "running", "ran", "None of the above"],
  },
  {
    numb: 16,
    question: "What is the superlative form of the adjective 'happy'?",
    answer: "happiest",
    options: ["happy", "happier", "happilier", "happiest"],
  },
  {
    numb: 17,
    question: "What is the antonym of 'beautiful'?",
    answer: "ugly",
    options: ["pretty", "ugly", "colorful", "happy"],
  },
  {
    numb: 18,
    question: "What is the present tense of 'was'?",
    answer: "is",
    options: ["be", "were", "is", "am"],
  },
  {
    numb: 19,
    question: "Which sentence is grammatically incorrect?",
    answer: "She had ate dinner.",
    options: [
      "She had ate dinner.",
      "They are swimming in the pool.",
      "He plays soccer every Saturday.",
      "We goes to the park.",
    ],
  },
  {
    numb: 20,
    question: "What is the antonym of 'happy'?",
    answer: "sad",
    options: ["sad", "joyful", "fast", "cold"],
  },
  {
    numb: 21,
    question:
      "What part of speech is the word 'quickly' in the sentence: 'She ran quickly to catch the bus'?",
    answer: "adverb",
    options: ["adjective", "verb", "adverb", "noun"],
  },
  {
    numb: 22,
    question: "Which sentence is a compound sentence?",
    answer: "I like ice cream, and he likes cake.",
    options: [
      "He walked to the store.",
      "She sings beautifully.",
      "I like ice cream, and he likes cake.",
      "They are reading books.",
    ],
  },
  {
    numb: 23,
    question: "What is the plural form of 'fox'?",
    answer: "foxes",
    options: ["foxes", "foxs", "foxies", "None of the above"],
  },
  {
    numb: 24,
    question:
      "Identify the conjunction in the sentence: 'I want to go to the movies, but I don't have any money.'",
    answer: "but",
    options: ["I", "to", "but", "any"],
  },
  {
    numb: 25,
    question: "What is the past participle of the verb 'swim'?",
    answer: "swum",
    options: ["swimmed", "swimming", "swum", "swim"],
  },
  {
    numb: 26,
    question: "Which sentence is in the future tense?",
    answer: "They will visit the museum tomorrow.",
    options: [
      "He ate breakfast.",
      "They will visit the museum tomorrow.",
      "She is singing a song.",
      "We went to the park.",
    ],
  },
  {
    numb: 27,
    question: "What is the possessive form of 'cat'?",
    answer: "cat's",
    options: ["cat's", "cats'", "cates", "None of the above"],
  },
  {
    numb: 28,
    question: "What is the comparative form of the adjective 'tall'?",
    answer: "taller",
    options: ["tall", "taller", "tallier", "tallest"],
  },
  {
    numb: 29,
    question: "Which of the following is a proper noun?",
    answer: "New York City",
    options: ["book", "mountain", "New York City", "quickly"],
  },
  {
    numb: 30,
    question:
      "What is the correct verb tense in the sentence: 'She has already eaten lunch'?",
    answer: "present perfect tense",
    options: [
      "past tense",
      "present tense",
      "future tense",
      "present perfect tense",
    ],
  },
  {
    numb: 31,
    question: "What is the singular form of 'mice'?",
    answer: "mouse",
    options: ["mices", "mice", "mousy", "None of the above"],
  },
  {
    numb: 32,
    question:
      "Identify the interjection in the sentence: 'Wow, that was amazing!'",
    answer: "Wow",
    options: ["that", "was", "amazing", "Wow"],
  },
  {
    numb: 33,
    question: "What is the future tense of 'read'?",
    answer: "will read",
    options: ["readed", "reading", "will read", "reads"],
  },
  {
    numb: 34,
    question: "What is the correct plural form of 'woman'?",
    answer: "women",
    options: ["womens", "womans", "women", "None of the above"],
  },
  {
    numb: 35,
    question: "Which sentence is in the active voice?",
    answer: "He wrote a beautiful song.",
    options: [
      "The cake was eaten by him.",
      "She was awarded a medal.",
      "They were surprised by the news.",
      "He wrote a beautiful song.",
    ],
  },
  {
    numb: 36,
    question: "What is the comparative form of 'good'?",
    answer: "better",
    options: ["good", "better", "gooder", "best"],
  },
  {
    numb: 37,
    question: "What is the possessive form of 'children'?",
    answer: "children's",
    options: ["child's", "childrens", "children's", "childs"],
  },
  {
    numb: 38,
    question:
      "Identify the article in the sentence: 'An apple fell from the tree.'",
    answer: "an",
    options: ["apple", "from", "the", "an"],
  },
  {
    numb: 39,
    question: "What is the singular form of 'geese'?",
    answer: "goose",
    options: ["gooses", "goose", "geese", "goosie"],
  },
  {
    numb: 40,
    question: "Which sentence is a complex sentence?",
    answer: "Although it rained, we went for a walk.",
    options: [
      "I like pizza.",
      "He went to the store, and he bought some milk.",
      "Although it rained, we went for a walk.",
      "She dances beautifully.",
    ],
  },
  {
    numb: 41,
    question: "What is the present tense of 'run'?",
    answer: "run",
    options: ["ran", "run", "runs", "running"],
  },
  {
    numb: 42,
    question: "What is the plural form of 'cherry'?",
    answer: "cherries",
    options: ["cherrys", "cherry", "cherries", "cheries"],
  },
  {
    numb: 43,
    question:
      "Identify the direct object in the sentence: 'She bought a new car.'",
    answer: "car",
    options: ["She", "bought", "new", "car"],
  },
  {
    numb: 44,
    question: "What is the past tense of the verb 'drive'?",
    answer: "drove",
    options: ["driving", "drived", "drove", "driven"],
  },
  {
    numb: 45,
    question: "What is the superlative form of 'bad'?",
    answer: "worst",
    options: ["bad", "worse", "worst", "badly"],
  },
  {
    numb: 46,
    question: "Which of the following is a synonym for 'smart'?",
    answer: "clever",
    options: ["clever", "slow", "loud", "strong"],
  },
  {
    numb: 47,
    question: "What is the future tense of 'sing'?",
    answer: "will sing",
    options: ["sang", "sung", "will sing", "singing"],
  },
  {
    numb: 48,
    question: "What is the antonym of 'happy'?",
    answer: "sad",
    options: ["sad", "joyful", "fast", "cold"],
  },
  {
    numb: 49,
    question:
      "What is the correct verb tense in the sentence: 'She is reading a book'?",
    answer: "present tense",
    options: [
      "past tense",
      "present tense",
      "future tense",
      "present perfect tense",
    ],
  },
  {
    numb: 50,
    question: "What is the singular form of 'knives'?",
    answer: "knife",
    options: ["knifes", "knive", "knife", "knifey"],
  },
];
