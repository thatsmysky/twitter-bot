# Twitter Bot Test 1
# Star Trek Episode Generator
# Lucy Kull

import tweepy
import random
import os
from secrets import *
from time import gmtime, strftime


bot_username = 'SpamsLot'
logfile_name = bot_username + ".log"

# list of verbs
verb = ["accept", "ache", "acknowledge", "act", "add", "admire", "admit", "admonish", "advise", "adopt", "affirm",
        "afford", "agree", "ail", "alert", "allege", "allow", "allude", "amuse", "analyze", "announce", "annoy",
        "answer", "apologize", "appeal", "appear", "applaud", "appreciate", "approve", "argue", "arrange", "arrest",
        "arrive", "articulate", "ask", "assert", "assure", "attach", "attack", "attempt", "attend", "attract",
        "auction", "avoid", "avow", "awake", "babble", "back", "bake", "balance", "balk", "ban", "bang", "bandage",
        "bar", "bare", "bargain", "bark",
        "barrage", "barter", "baste", "bat", "bathe", "battle", "bawl", "be", "beam", "bear", "beat", "become",
        "befriend", "beg", "begin", "behave", "believe", "bellow", "belong", "bend", "berate", "besiege", "bestow",
        "bet", "bid", "bite", "bleach", "bleed", "bless", "blind", "blink", "blot", "blow", "blurt", "blush",
        "boast", "bob", "boil", "bolt", "bomb", "book", "bore", "borrow", "bounce", "bow", "box", "brag", "brake",
        "branch", "brand", "break", "breathe", "breed", "bring", "broadcast", "broil", "bruise", "brush", "bubble",
        "build", "bump", "burn", "burnish", "bury", "buy", "buzz", "cajole", "calculate", "call", "camp", "care",
        "carry", "carve", "cause", "caution", "catch", "challenge",
        "change", "chant", "charge", "chase", "cheat", "check", "cheer", "chew", "chide", "chip", "choke", "chomp",
        "choose", "chop", "claim", "clap", "clean", "clear", "climb", "clip", "close", "coach", "coil", "collect",
        "color", "comb", "come", "comfort", "command", "comment", "communicate", "compare", "compete", "complain",
        "complete", "concede", "concentrate", "concern", "conclude", "concur", "confess", "confide", "confirm",
        "connect", "consent", "consider", "consist", "contain", "contend", "continue", "cook", "copy", "correct",
        "cost", "cough", "count", "counter", "cover", "covet", "crack", "crash", "crave", "crawl", "crochet",
        "cross", "criticize", "croak", "cross-examine", "crowd", "crush", "cry", "cure", "curl", "curse", "curve",
        "cut", "cycle", "dam", "damage", "dance", "dare", "deal", "debate", "decay", "deceive", "decide", "decipher",
        "declare",
        "decorate", "delay", "delight", "deliver", "demand", "deny", "depend", "describe", "desert", "deserve",
        "desire", "deter", "develop", "dial", "dictate", "die", "dig", "digress", "direct", "disclose", "dislike",
        "dive", "divide", "divorce", "divulge", "do", "dock", "dole", "dote", "double", "doubt", "drag", "drain",
        "draw", "dream", "dress", "drip", "drill", "drink", "drive", "drone", "drop", "drown", "dry", "dupe", "dump",
        "dust", "dye""earn", "eat", "echo", "edit", "educate", "elope", "embarrass", "emigrate", "emit", "emphasize",
        "employ",
        "empty", "enchant", "encode", "encourage", "end", "enjoin", "enjoy", "enter", "entertain", "enunciate", "envy",
        "equivocate", "escape", "evacuate", "evaporate", "exaggerate", "examine", "excite", "exclaim", "excuse",
        "exercise", "exist", "expand", "expect", "expel", "exhort", "explain", "explode", "explore", "extend",
        "face", "fade", "fail", "fall", "falter", "fasten", "favor", "fax", "fear", "feed", "feel", "fence", "fetch",
        "fight", "file", "fill", "film", "find", "fire", "fish", "fit", "fix", "flap", "flash", "flee", "float",
        "flood", "floss", "flow", "flower", "fly", "fold", "follow", "fool", "force", "foretell", "forget", "forgive",
        "form", "found", "frame", "freeze", "fret", "frighten", "fry", "fume", "garden", "gasp", "gather", "gaze",
        "gel", "get", "gild", "give", "glide", "glue", "gnaw", "go", "grab", "grate", "grease", "greet", "grill",
        "grin", "grip", "groan", "grow", "growl", "grumble", "grunt", "guarantee", "guard", "guess", "guide", "gurgle",
        "gush", "hail", "hammer", "hand", "handle", "hang", "happen", "harass", "harm", "harness", "hate", "haunt",
        "have", "head", "heal", "heap", "hear", "heat", "help", "hide", "highlight", "hijack", "hinder", "hint",
        "hiss", "hit", "hold", "hook", "hoot", "hop", "hope", "hover", "howl", "hug", "hum", "hunt", "hurry", "hurt",
        "ice", "identify", "ignore", "imagine", "immigrate", "imply", "implore", "impress", "improve", "include",
        "increase", "infect", "inflate", "influence", "inform", "infuse", "inject", "injure", "inquire", "insist",
        "inspect", "inspire", "instruct", "intend", "interest", "interfere", "interject", "interrupt", "introduce",
        "invent", "invest", "invite", "irritate", "iron", "itch", "jab", "jabber", "jail", "jam", "jeer", "jest",
        "jog", "join", "joke", "jolt", "judge", "juggle", "jump", "keep", "kick", "kill", "kiss", "kneel", "knit",
        "knock", "knot", "know", "label", "lament", "land", "last", "laugh", "lay", "lead", "lean", "learn", "leave",
        "lecture", "lend", "let", "level", "license", "lick", "lie", "lift", "light", "lighten", "like", "list",
        "listen", "live", "load", "loan", "lock", "long", "look", "loosen", "lose", "love", "lower", "mail",
        "maintain", "make", "man", "manage", "mar", "march", "mark", "marry", "marve", "mate", "matter", "mean",
        "measure", "meet", "melt", "memorize", "mend", "mention", "merge", "milk", "mine", "miss", "mix", "moan",
        "moor", "mourn", "molt", "move", "mow", "mug", "multiply", "mumble", "murder", "mutter", "nag", "nail", "name",
        "nap", "need", "nest", "nod", "note", "notice", "number", "obey", "object", "observe", "obtain", "occur",
        "offend", "offer", "ogle", "oil", "omit", "open", "operate", "order", "overflow", "overrun", "owe", "own",
        "pack", "pad", "paddle", "paint", "pant", "park", "part", "pass", "paste", "pat", "pause", "pay", "peck",
        "pedal", "peel", "peep", "peer", "peg", "pelt", "perform", "permit", "pester", "pet", "phone", "pick", "pinch",
        "pine", "place", "plan", "plant", "play", "plead", "please", "pledge", "plow", "plug", "point", "poke",
        "polish", "ponder", "pop", "possess", "post", "postulate", "pour", "practice", "pray", "preach", "precede",
        "predict", "prefer", "prepare", "present", "preserve", "press", "pretend", "prevent", "prick", "print",
        "proceed", "proclaim", "produce", "profess", "program", "promise", "propose", "protect", "protest", "provide",
        "pry", "pull", "pump", "punch", "puncture", "punish", "push", "put", "question", "quilt", "quit", "quiz",
        "quote", "race", "radiate", "rain", "raise", "rant", "rain", "rate", "rave", "reach", "realize", "read",
        "rebuff", "recall", "receive", "recite", "recognize", "recommend", "record", "reduce", "reflect", "refuse",
        "regret", "reign", "reiterate", "reject", "rejoice", "relate", "relax", "release", "rely", "remain",
        "remember", "remind", "remove", "repair", "repeat", "replace", "reply", "report", "reprimand", "reproduce",
        "request", "rescue", "retire", "retort", "return", "reveal", "reverse", "rhyme", "ride", "ring", "rinse",
        "rise", "risk", "roar", "rob", "rock", "roll", "row", "rub", "ruin", "rule", "run", "rush", "sack", "sail",
        "satisfy", "save", "savor", "saw", "say", "scare", "scatter", "scoff", "scold", "scoot", "scorch", "scrape",
        "scratch", "scream", "screech", "screw", "scribble", "seal", "search", "see", "sell", "send", "sense",
        "separate", "serve", "set", "settle", "sever", "sew", "shade", "shampoo", "share", "shave", "shelter", "shift",
        "shiver", "shock", "shoot", "shop", "shout", "show", "shriek", "shrug", "shut", "sigh", "sign", "signal",
        "sin", "sing", "singe", "sip", "sit", "skate", "skateboard", "sketch", "ski", "skip", "slap", "sleep", "slice",
        "slide", "slip", "slow", "smash", "smell", "smile", "smoke", "snap", "snarl", "snatch", "sneak", "sneer",
        "sneeze", "snicker", "sniff", "snore", "snort", "snoop", "snooze", "snow", "soak", "sob", "soothe", "sound",
        "sow", "span", "spare", "spark", "sparkle", "speak", "speculate", "spell", "spend", "spill", "spin", "spoil",
        "spot", "spray", "sprout", "sputter", "squash", "squeeze", "stab", "stain", "stammer", "stamp", "stand",
        "star", "stare", "start", "stash", "state", "stay", "steer", "step", "stipulate", "stir", "stitch", "stop",
        "store", "strap", "storm", "stow", "strengthen", "stress", "stretch", "strip", "stroke", "stuff", "stutter",
        "stray", "strum", "strut", "stun", "stunt", "submerge", "succeed", "suffer", "suggest", "suit", "supply",
        "support", "suppose", "surmise", "surprise", "surround", "suspect", "suspend", "sway", "swear", "swim",
        "swing", "switch", "swoop", "sympathize", "talk", "take", "tame", "tap", "taste", "taunt", "teach", "tear",
        "tease", "telephone", "tell", "tempt", "terrify", "test", "testify", "thank", "thaw", "theorize", "think",
        "threaten", "throw", "thunder", "tick", "tickle", "tie", "time", "tip", "tire", "toast", "toss", "touch",
        "tour", "tow", "trace", "track", "trade", "train", "translate", "transport", "trap", "travel", "treat",
        "tremble", "trick", "trickle", "trim", "trip", "trot", "trouble", "trust", "trounce", "try", "tug", "tumble",
        "turn", "twist", "type", "understand", "undress", "unfasten", "unite", "unlock", "unpack", "uphold", "upset",
        "upstage", "urge", "untie", "use", "usurp", "utter", "vacuum", "value", "vanish", "vanquish", "venture",
        "visit", "voice", "volunteer", "vote", "vouch", "wail", "wait", "wake", "walk", "wallow", "wander", "want",
        "warm", "warn", "wash", "waste", "watch", "water", "wave", "waver", "wear", "weave", "wed", "weigh", "welcome",
        "whimper", "whine", "whip", "whirl", "whisper", "whistle", "win", "wink", "wipe", "wish", "wobble", "wonder",
        "work", "worry", "wrap", "wreck", "wrestle", "wriggle", "write", "writhe", "x-ray", "yawn", "yell", "yelp",
        "yield", "yodel", "zip", "zoom"]


# list of nouns
noun = ["account", "achiever", "acoustics", "act", "action", "activity", "actor", "addition", "adjustment",
        "advertisement", "advice", "aftermath", "afternoon", "afterthought", "agreement", "air", "airplane", "airport",
        "alarm", "amount", "amusement", "anger", "angle", "animal", "answer", "ant", "ants", "apparatus", "apparel",
        "apple", "apples", "appliance", "approval", "arch", "argument", "arithmetic", "arm", "army", "art", "attack",
        "attempt", "attention", "attraction", "aunt", "authority", "babies", "baby", "back", "badge", "bag", "bait",
        "balance", "ball", "balloon", "balls", "banana", "band", "base", "baseball", "basin", "basket", "basketball",
        "bat", "bath", "battle", "bead", "beam", "bean", "bear", "bears", "beast", "bed", "bedroom", "beds", "bee",
        "beef", "beetle", "beggar", "beginner", "behavior", "belief", "believe", "bell", "bells", "berry", "bike",
        "bikes", "bird", "birds", "birth", "birthday", "bit", "bite", "blade", "blood", "blow", "board", "boat",
        "boats", "body", "bomb", "bone", "book", "books", "boot", "border", "bottle", "boundary", "box", "boy", "boys",
        "brain", "brake", "branch", "brass", "bread", "breakfast", "breath", "brick", "bridge", "brother", "brothers",
        "brush", "bubble", "bucket", "building", "bulb", "bun", "burn", "burst", "bushes", "business", "butter",
        "button", "cabbage", "cable", "cactus", "cake", "cakes", "calculator", "calendar", "camera", "camp", "can",
        "cannon", "canvas", "cap", "caption", "car", "card", "care", "carpenter", "carriage", "cars", "cart", "cast",
        "cat", "cats", "cattle", "cause", "cave", "celery", "cellar", "cemetery", "cent", "chain", "chair", "chairs",
        "chalk", "chance", "change", "channel", "cheese", "cherries", "cherry", "chess", "chicken", "chickens",
        "children", "chin", "church", "circle", "clam", "class", "clock", "clocks", "cloth", "cloud", "clouds",
        "clover", "club", "coach", "coal", "coast", "coat", "cobweb", "coil", "collar", "color", "comb", "comfort",
        "committee", "company", "comparison", "competition", "condition", "connection", "control", "cook", "copper",
        "copy", "cord", "cork", "corn", "cough", "country", "cover", "cow", "cows", "crack", "cracker", "crate",
        "crayon", "cream", "creator", "creature", "credit", "crib", "crime", "crook", "crow", "crowd", "crown", "crush",
        "cry", "cub", "cup", "current", "curtain", "curve", "cushion", "dad", "daughter", "day", "death", "debt",
        "decision", "deer", "degree", "design", "desire", "desk", "destruction", "detail", "development", "digestion",
        "dime", "dinner", "dinosaurs", "direction", "dirt", "discovery", "discussion", "disease", "disgust", "distance",
        "distribution", "division", "dock", "doctor", "dog", "dogs", "doll", "dolls", "donkey", "door", "downtown",
        "drain", "drawer", "dress", "drink", "driving", "drop", "drug", "drum", "duck", "ducks", "dust", "ear", "earth",
        "earthquake", "edge", "education", "effect", "egg", "eggnog", "eggs", "elbow", "end", "engine", "error",
        "event", "example", "exchange", "existence", "expansion", "experience", "expert", "eye", "eyes", "face", "fact",
        "fairies", "fall", "family", "fan", "fang", "farm", "farmer", "father", "father", "faucet", "fear", "feast",
        "feather", "feeling", "feet", "fiction", "field", "fifth", "fight", "finger", "fire", "fireman", "fish", "flag",
        "flame", "flavor", "flesh", "flight", "flock", "floor", "flower", "flowers", "fly", "fog", "fold", "food",
        "foot", "force", "fork", "form", "fowl", "frame", "friction", "friend", "friends", "frog", "frogs", "front",
        "fruit", "fuel", "furniture", "game", "garden", "gate", "geese", "ghost", "giants", "giraffe", "girl", "girls",
        "glass", "glove", "glue", "goat", "gold", "goldfish", "good-bye", "goose", "government", "governor", "grade",
        "grain", "grandfather", "grandmother", "grape", "grass", "grip", "ground", "group", "growth", "guide", "guitar",
        "gun", "hair", "haircut", "hall", "hammer", "hand", "hands", "harbor", "harmony", "hat", "hate", "head",
        "health", "hearing", "heart", "heat", "help", "hen", "hill", "history", "hobbies", "hole", "holiday", "home",
        "honey", "hook", "hope", "horn", "horse", "horses", "hose", "hospital", "hot", "hour", "house", "houses",
        "humor", "hydrant", "ice", "icicle", "idea", "impulse", "income", "increase", "industry", "ink", "insect",
        "instrument", "insurance", "interest", "invention", "iron", "island", "jail", "jam", "jar", "jeans", "jelly",
        "jellyfish", "jewel", "join", "joke", "journey", "judge", "juice", "jump", "kettle", "key", "kick", "kiss",
        "kite", "kitten", "kitty", "knee", "knife", "knot", "knowledge", "laborer", "lace", "ladybug", "lake", "lamp",
        "land", "language", "laugh", "lawyer", "lead", "leaf", "learning", "leather", "leg", "legs", "letter",
        "letters", "lettuce", "level", "library", "lift", "light", "limit", "line", "linen", "lip", "liquid", "list",
        "lizards", "loaf", "lock", "locket", "look", "loss", "love", "low", "lumber", "lunch", "lunchroom", "machine",
        "magic", "maid", "mailbox", "man", "manager", "map", "marble", "mark", "market", "mask", "mass", "match",
        "meal", "measure", "meat", "meeting", "memory", "men", "metal", "mice", "middle", "milk", "mind", "mine",
        "minister", "mint", "minute", "mist", "mitten", "mom", "money", "monkey", "month", "moon", "morning", "mother",
        "motion", "mountain", "mouth", "move", "muscle", "music", "nail", "name", "nation", "neck", "need", "needle",
        "nerve", "nest", "net", "news", "night", "noise", "north", "nose", "note", "notebook", "number", "nut",
        "oatmeal", "observation", "ocean", "offer", "office", "oil", "operation", "opinion", "orange", "oranges",
        "order", "organization", "ornament", "oven", "owl", "owner", "page", "pail", "pain", "paint", "pan", "pancake",
        "paper", "parcel", "parent", "park", "part", "partner", "party", "passenger", "paste", "patch", "payment",
        "peace", "pear", "pen", "pencil", "person", "pest", "pet", "pets", "pickle", "picture", "pie", "pies", "pig",
        "pin", "pipe", "pizzas", "place", "plane", "planes", "plant", "plantation", "plants", "plastic", "plate",
        "play", "playground", "pleasure", "plot", "plough", "pocket", "point", "poison", "police", "polish",
        "pollution", "popcorn", "porter", "position", "pot", "potato", "powder", "power", "price", "print", "prison",
        "process", "produce", "profit", "property", "prose", "protest", "pull", "pump", "punishment", "purpose", "push",
        "quarter", "quartz", "queen", "question", "quicksand", "quiet", "quill", "quilt", "quince", "quiver", "rabbit",
        "rail", "railway", "rain", "rainstorm", "rake", "range", "rat", "rate", "ray", "reaction", "reading", "reason",
        "receipt", "recess", "record", "regret", "relation", "religion", "representative", "request", "respect",
        "rest", "reward", "rhythm", "rice", "riddle", "rifle", "ring", "river", "road", "robin", "rock", "rod", "roll",
        "roof", "room", "root", "rose", "route", "rub", "rule", "run", "sack", "sail", "salt", "sand", "scale",
        "scarecrow", "scarf", "scene", "scent", "school", "science", "scissors", "screw", "sea", "seashore", "seat",
        "secretary", "selection", "self", "sense", "servant", "shade", "shake", "shame", "shape", "sheep", "sheet",
        "shelf", "ship", "shirt", "shock", "shoe", "shop", "show", "side", "sidewalk", "sign", "silk", "silver", "sink",
        "sister", "size", "skate", "skin", "skirt", "sky", "slave", "sleep", "sleet", "slip", "slope", "smash", "smell",
        "smile", "smoke", "snail", "snake", "sneeze", "snow", "soap", "society", "sock", "soda", "sofa", "son", "song",
        "sort", "sound", "soup", "space", "spade", "spark", "sponge", "spoon", "spot", "spring", "spy", "square",
        "squirrel", "stage", "stamp", "star", "start", "statement", "station", "steam", "steel", "stem", "step", "stew",
        "stick", "stitch", "stocking", "stomach", "stone", "stop", "store", "story", "stove", "stranger", "straw",
        "stream", "street", "stretch", "string", "structure", "substance", "sugar", "suggestion", "suit", "summer",
        "sun", "support", "surprise", "sweater", "swim", "swing", "system", "table", "tail", "talk", "tank", "taste",
        "tax", "teaching", "team", "teeth", "temper", "tendency", "tent", "territory", "test", "texture", "theory",
        "thing", "things", "thought", "thread", "thrill", "throat", "throne", "thumb", "thunder", "ticket", "tiger",
        "time", "tin", "title", "toad", "toe", "toes", "tongue", "tooth", "toothbrush", "toothpaste", "top", "touch",
        "town", "toy", "trade", "trail", "train", "tramp", "transport", "tray", "treatment", "tree", "trick", "trip",
        "trouble", "trousers", "truck", "tub", "turkey", "turn", "twig", "twist", "umbrella", "uncle", "underwear",
        "unit", "use", "vacation", "value", "van", "vase", "vegetable", "veil", "vein", "verse", "vessel", "vest",
        "view", "visitor", "voice", "volcano", "volleyball", "voyage", "walk", "wall", "war", "wash", "waste", "watch",
        "water", "wave", "waves", "wax", "way", "wealth", "weather", "week", "weight", "wheel", "whip", "whistle",
        "wilderness", "wind", "window", "wine", "wing", "winter", "wire", "wish", "woman", "wood", "wool", "word",
        "work", "worm", "wound", "wren", "wrench", "wrist", "writer", "writing", "yak", "yam", "yard", "yarn", "year",
        "yoke", "zebra", "zephyr", "zinc", "zipper", "zoo"]


# list of adjectives
adjective = ["abandoned", "able", "absolute", "adorable", "adventurous", "academic", "acceptable", "acclaimed",
             "accomplished", "accurate", "aching", "acidic", "acrobatic", "active", "actual", "adept", "admirable",
             "admired", "adolescent", "adorable", "adored", "advanced", "afraid", "affectionate", "aged", "aggravating",
             "aggressive", "agile", "agitated", "agonizing", "agreeable", "ajar", "alarmed", "alarming", "alert",
             "alienated", "alive", "all", "altruistic", "amazing", "ambitious", "ample", "amused", "amusing",
             "anchored", "ancient", "angelic", "angry", "anguished", "animated", "annual", "another", "antique",
             "anxious", "any", "apprehensive", "appropriate", "apt", "arctic", "arid", "aromatic", "artistic",
             "ashamed", "assured", "astonishing", "athletic", "attached", "attentive", "attractive", "austere",
             "authentic", "authorized", "automatic", "avaricious", "average", "aware", "awesome", "awful", "awkward",
             "babyish", "bad", "back", "baggy", "bare", "barren", "basic", "beautiful", "belated", "beloved",
             "beneficial", "better", "best", "bewitched", "big", "big-hearted", "biodegradable", "bite-sized",
             "bitter", "black", "black-and-white", "bland", "blank", "blaring", "bleak", "blind", "blissful", "blond",
             "blue", "blushing", "bogus", "boiling", "bold", "bony", "boring", "bossy", "both", "bouncy", "bountiful",
             "bowed", "brave", "breakable", "brief", "bright", "brilliant", "brisk", "broken", "bronze", "brown",
             "bruised", "bubbly", "bulky", "bumpy", "buoyant", "burdensome", "burly", "bustling", "busy", "buttery",
             "buzzing", "calculating", "calm", "candid", "canine", "capital", "carefree", "careful", "careless",
             "caring", "cautious", "cavernous", "celebrated", "charming", "cheap", "cheerful", "cheery", "chief",
             "chilly", "chubby", "circular", "classic", "clean", "clear", "clear-cut", "clever", "close", "closed",
             "cloudy", "clueless", "clumsy", "cluttered", "coarse", "cold", "colorful", "colorless", "colossal",
             "comfortable", "common", "compassionate", "competent", "complete", "complex", "complicated", "composed",
             "concerned", "concrete", "confused", "conscious", "considerate", "constant", "content", "conventional",
             "cooked", "cool", "cooperative", "coordinated", "corny", "corrupt", "costly", "courageous", "courteous",
             "crafty", "crazy", "creamy", "creative", "creepy", "criminal", "crisp", "critical", "crooked", "crowded",
             "cruel", "crushing", "cuddly", "cultivated", "cultured", "cumbersome", "curly", "curvy", "cute",
             "cylindrical", "damaged", "damp", "dangerous", "dapper", "daring", "darling", "dark", "dazzling", "dead",
             "deadly", "deafening", "dear", "dearest", "decent", "decimal", "decisive", "deep", "defenseless",
             "defensive", "defiant", "deficient", "definite", "definitive", "delayed", "delectable", "delicious",
             "delightful", "delirious", "demanding", "dense", "dental", "dependable", "dependent", "descriptive",
             "deserted", "detailed", "determined", "devoted", "different", "difficult", "digital", "diligent", "dim",
             "dimpled", "dimwitted", "direct", "disastrous", "discrete", "disfigured", "disgusting", "disloyal",
             "dismal", "distant", "downright", "dreary", "dirty", "disguised", "dishonest", "dismal", "distant",
             "distinct", "distorted", "dizzy", "dopey", "doting", "double", "downright", "drab", "drafty", "dramatic",
             "dreary", "droopy", "dry", "dual", "dull", "dutiful", "each", "eager", "earnest", "early", "easy",
             "easy-going", "ecstatic", "edible", "educated", "elaborate", "elastic", "elated", "elderly", "electric",
             "elegant", "elementary", "elliptical", "embarrassed", "embellished", "eminent", "emotional", "empty",
             "enchanted", "enchanting", "energetic", "enlightened", "enormous", "enraged", "entire", "envious", "equal",
             "equatorial", "essential", "esteemed", "ethical", "euphoric", "even", "evergreen", "everlasting", "every",
             "evil", "exalted", "excellent", "exemplary", "exhausted", "excitable", "excited", "exciting", "exotic",
             "expensive", "experienced", "expert", "extraneous", "extroverted", "extra-large", "extra-small",
             "fabulous", "failing", "faint", "fair", "faithful", "fake", "false", "familiar", "famous", "fancy",
             "fantastic", "far", "faraway", "far-flung", "far-off", "fast", "fat", "fatal", "fatherly", "favorable",
             "favorite", "fearful", "fearless", "feisty", "feline", "female", "feminine", "few", "fickle", "filthy",
             "fine", "finished", "firm", "first", "firsthand", "fitting", "fixed", "flaky", "flamboyant", "flashy",
             "flat", "flawed", "flawless", "flickering", "flimsy", "flippant", "flowery", "fluffy", "fluid",
             "flustered", "focused", "fond", "foolhardy", "foolish", "forceful", "forked", "formal", "forsaken",
             "forthright", "fortunate", "fragrant", "frail", "frank", "frayed", "free", "French", "fresh", "frequent",
             "friendly", "frightened", "frightening", "frigid", "frilly", "frizzy", "frivolous", "front", "frosty",
             "frozen", "frugal", "fruitful", "full", "fumbling", "functional", "funny", "fussy", "fuzzy", "gargantuan",
             "gaseous", "general", "generous", "gentle", "genuine", "giant", "giddy", "gigantic", "gifted", "giving",
             "glamorous", "glaring", "glass", "gleaming", "gleeful", "glistening", "glittering", "gloomy", "glorious",
             "glossy", "glum", "golden", "good", "good-natured", "gorgeous", "graceful", "gracious", "grand",
             "grandiose", "granular", "grateful", "grave", "gray", "great", "greedy", "green", "gregarious", "grim",
             "grimy", "gripping", "grizzled", "gross", "grotesque", "grouchy", "grounded", "growing", "growling",
             "grown", "grubby", "gruesome", "grumpy", "guilty", "gullible", "gummy", "hairy", "half", "handmade",
             "handsome", "handy", "happy", "happy-go-lucky", "hard", "hard-to-find", "harmful", "harmless",
             "harmonious", "harsh", "hasty", "hateful", "haunting", "healthy", "heartfelt", "hearty", "heavenly",
             "heavy", "hefty", "helpful", "helpless", "hidden", "hideous", "high", "high-level", "hilarious", "hoarse",
             "hollow", "homely", "honest", "honorable", "honored", "hopeful", "horrible", "hospitable", "hot", "huge",
             "humble", "humiliating", "humming", "humongous", "hungry", "hurtful", "husky", "icky", "icy", "ideal",
             "idealistic", "identical", "idle", "idiotic", "idolized", "ignorant", "ill", "illegal", "ill-fated",
             "ill-informed", "illiterate", "illustrious", "imaginary", "imaginative", "immaculate", "immaterial",
             "immediate", "immense", "impassioned", "impeccable", "impartial", "imperfect", "imperturbable", "impish",
             "impolite", "important", "impossible", "impractical", "impressionable", "impressive", "improbable",
             "impure", "inborn", "incomparable", "incompatible", "incomplete", "inconsequential", "incredible",
             "indelible", "inexperienced", "indolent", "infamous", "infantile", "infatuated", "inferior", "infinite",
             "informal", "innocent", "insecure", "insidious", "insignificant", "insistent", "instructive",
             "insubstantial", "intelligent", "intent", "intentional", "interesting", "internal", "international",
             "intrepid", "ironclad", "irresponsible", "irritating", "itchy", "jaded", "jagged", "jam-packed", "jaunty",
             "jealous", "jittery", "joint", "jolly", "jovial", "joyful", "joyous", "jubilant", "judicious", "juicy",
             "jumbo", "junior", "jumpy", "juvenile", "kaleidoscopic", "keen", "key", "kind", "kindhearted", "kindly",
             "klutzy", "knobby", "knotty", "knowledgeable", "knowing", "known", "kooky", "kosher", "lame", "lanky",
             "large", "last", "lasting", "late", "lavish", "lawful", "lazy", "leading", "lean", "leafy", "left",
             "legal", "legitimate", "light", "lighthearted", "likable", "likely", "limited", "limp", "limping",
             "linear", "lined", "liquid", "little", "live", "lively", "livid", "loathsome", "lone", "lonely", "long",
             "long-term", "loose", "lopsided", "lost", "loud", "lovable", "lovely", "loving", "low", "loyal", "lucky",
             "lumbering", "luminous", "lumpy", "lustrous", "luxurious", "mad", "made-up", "magnificent", "majestic",
             "major", "male", "mammoth", "married", "marvelous", "masculine", "massive", "mature", "meager", "mealy",
             "mean", "measly", "meaty", "medical", "mediocre", "medium", "meek", "mellow", "melodic", "memorable",
             "menacing", "merry", "messy", "metallic", "mild", "milky", "mindless", "miniature", "minor", "minty",
             "miserable", "miserly", "misguided", "misty", "mixed", "modern", "modest", "moist", "monstrous", "monthly",
             "monumental", "moral", "mortified", "motherly", "motionless", "mountainous", "muddy", "muffled",
             "multicolored", "mundane", "murky", "mushy", "musty", "muted", "mysterious", "naive", "narrow", "nasty",
             "natural", "naughty", "nautical", "near", "neat", "necessary", "needy", "negative", "neglected",
             "negligible", "neighboring", "nervous", "new", "next", "nice", "nifty", "nimble", "nippy", "nocturnal",
             "noisy", "nonstop", "normal", "notable", "noted", "noteworthy", "novel", "noxious", "numb", "nutritious",
             "nutty", "obedient", "obese", "oblong", "oily", "oblong", "obvious", "occasional", "odd", "oddball",
             "offbeat", "offensive", "official", "old", "old-fashioned", "only", "open", "optimal", "optimistic",
             "opulent", "orange", "orderly", "organic", "ornate", "ornery", "ordinary", "original", "other", "our",
             "outlying", "outgoing", "outlandish", "outrageous", "outstanding", "oval", "overcooked", "overdue",
             "overjoyed", "overlooked", "palatable", "pale", "paltry", "parallel", "parched", "partial", "passionate",
             "past", "pastel", "peaceful", "peppery", "perfect", "perfumed", "periodic", "perky", "personal",
             "pertinent", "pesky", "pessimistic", "petty", "phony", "physical", "piercing", "pink", "pitiful", "plain",
             "plaintive", "plastic", "playful", "pleasant", "pleased", "pleasing", "plump", "plush", "polished",
             "polite", "political", "pointed", "pointless", "poised", "poor", "popular", "portly", "posh", "positive",
             "possible", "potable", "powerful", "powerless", "practical", "precious", "present", "prestigious",
             "pretty", "precious", "previous", "pricey", "prickly", "primary", "prime", "pristine", "private", "prize",
             "probable", "productive", "profitable", "profuse", "proper", "proud", "prudent", "punctual", "pungent",
             "puny", "pure", "purple", "pushy", "putrid", "puzzled", "puzzling", "quaint", "qualified", "quarrelsome",
             "quarterly", "queasy", "querulous", "questionable", "quick", "quick-witted", "quiet", "quintessential",
             "quirky", "quixotic", "quizzical", "radiant", "ragged", "rapid", "rare", "rash", "raw", "recent",
             "reckless", "rectangular", "ready", "real", "realistic", "reasonable", "red", "reflecting", "regal",
             "regular", "reliable", "relieved", "remarkable", "remorseful", "remote", "repentant", "required",
             "respectful", "responsible", "repulsive", "revolving", "rewarding", "rich", "rigid", "right", "ringed",
             "ripe", "roasted", "robust", "rosy", "rotating", "rotten", "rough", "round", "rowdy", "royal", "rubbery",
             "rundown", "ruddy", "rude", "runny", "rural", "rusty", "sad", "safe", "salty", "same", "sandy", "sane",
             "sarcastic", "sardonic", "satisfied", "scaly", "scarce", "scared", "scary", "scented", "scholarly",
             "scientific", "scornful", "scratchy", "scrawny", "second", "secondary", "second-hand", "secret",
             "self-assured", "self-reliant", "selfish", "sentimental", "separate", "serene", "serious", "serpentine",
             "several", "severe", "shabby", "shadowy", "shady", "shallow", "shameful", "shameless", "sharp",
             "shimmering", "shiny", "shocked", "shocking", "shoddy", "short", "short-term", "showy", "shrill", "shy",
             "sick", "silent", "silky", "silly", "silver", "similar", "simple", "simplistic", "sinful", "single",
             "sizzling", "skeletal", "skinny", "sleepy", "slight", "slim", "slimy", "slippery", "slow", "slushy",
             "small", "smart", "smoggy", "smooth", "smug", "snappy", "snarling", "sneaky", "sniveling", "snoopy",
             "sociable", "soft", "soggy", "solid", "somber", "some", "spherical", "sophisticated", "sore", "sorrowful",
             "soulful", "soupy", "sour", "Spanish", "sparkling", "sparse", "specific", "spectacular", "speedy", "spicy",
             "spiffy", "spirited", "spiteful", "splendid", "spotless", "spotted", "spry", "square", "squeaky",
             "squiggly", "stable", "staid", "stained", "stale", "standard", "starchy", "stark", "starry", "steep",
             "sticky", "stiff", "stimulating", "stingy", "stormy", "straight", "strange", "steel", "strict", "strident",
             "striking", "striped", "strong", "studious", "stunning", "stupendous", "stupid", "sturdy", "stylish",
             "subdued", "submissive", "substantial", "subtle", "suburban", "sudden", "sugary", "sunny", "super",
             "superb", "superficial", "superior", "supportive", "sure-footed", "surprised", "suspicious", "svelte",
             "sweaty", "sweet", "sweltering", "swift", "sympathetic", "tall", "talkative", "tame", "tan", "tangible",
             "tart", "tasty", "tattered", "taut", "tedious", "teeming", "tempting", "tender", "tense", "tepid",
             "terrible", "terrific", "testy", "thankful", "that", "these", "thick", "thin", "third", "thirsty", "this",
             "thorough", "thorny", "those", "thoughtful", "threadbare", "thrifty", "thunderous", "tidy", "tight",
             "timely", "tinted", "tiny", "tired", "torn", "total", "tough", "traumatic", "treasured", "tremendous",
             "tragic", "trained", "tremendous", "triangular", "tricky", "trifling", "trim", "trivial", "troubled",
             "true", "trusting", "trustworthy", "trusty", "truthful", "tubby", "turbulent", "twin", "ugly", "ultimate",
             "unacceptable", "unaware", "uncomfortable", "uncommon", "unconscious", "understated", "unequaled",
             "uneven", "unfinished", "unfit", "unfolded", "unfortunate", "unhappy", "unhealthy", "uniform",
             "unimportant", "unique", "united", "unkempt", "unknown", "unlawful", "unlined", "unlucky", "unnatural",
             "unpleasant", "unrealistic", "unripe", "unruly", "unselfish", "unsightly", "unsteady", "unsung", "untidy",
             "untimely", "untried", "untrue", "unused", "unusual", "unwelcome", "unwieldy", "unwilling", "unwitting",
             "unwritten", "upbeat", "upright", "upset", "urban", "usable", "used", "useful", "useless", "utilized",
             "utter", "vacant", "vague", "vain", "valid", "valuable", "vapid", "variable", "vast", "velvety",
             "venerated", "vengeful", "verifiable", "vibrant", "vicious", "victorious", "vigilant", "vigorous",
             "villainous", "violet", "violent", "virtual", "virtuous", "visible", "vital", "vivacious", "vivid",
             "voluminous", "wan", "warlike", "warm", "warmhearted", "warped", "wary", "wasteful", "watchful",
             "waterlogged", "watery", "wavy", "wealthy", "weak", "weary", "webbed", "wee", "weekly", "weepy", "weighty",
             "weird", "welcome", "well-documented", "well-groomed", "well-informed", "well-lit", "well-made",
             "well-off", "well-to-do", "well-worn", "wet", "which", "whimsical", "whirlwind", "whispered", "white",
             "whole", "whopping", "wicked", "wide", "wide-eyed", "wiggly", "wild", "willing", "wilted", "winding",
             "windy", "winged", "wiry", "wise", "witty", "wobbly", "woeful", "wonderful", "wooden", "woozy", "wordy",
             "worldly", "worn", "worried", "worrisome", "worse", "worst", "worthless", "worthwhile", "worthy",
             "wrathful", "wretched", "writhing", "wrong", "wry", "yawning", "yearly", "yellow", "yellowish", "young",
             "youthful", "yummy", "zany", "zealous", "zesty", "zigzag"]



# list of characters for bot to draw from
st_character = ["Captain Kirk", "Commander Spock", "James T Kirk", "Spock", "Bones", "Leonard McCoy", "Doctor McCoy",
                "Montgomery Scott", "Scotty", "Lt. Commander Scott", "Hikaru Sulu", "Sulu", "Lt. Sulu", "Chekov",
                "Lt. Chekov", "Pavel Chekov", "Uhura", "Lt. Uhura", "Nyota Uhura", "Nurse Chapel", "Christine Chapel",
                "the USS Enterprise", "the Enterprise"]

# alt list of random names
rand_character = ["Jefferson", "Burr", "Hamilton", "Aaron Burr", "Alexander Hamilton", "Thomas Jefferson",
                  "Eliza Hamilton", "George Washington", "Angelica Hamilton", "Maria Reynolds", "Caroline", "Eileen",
                  "Annie Kate", "Sarah", "Cindy", "Bob", "Sam", "Emily", "Mary", "John", "James", "George", "Sally",
                  "Carly", "Josh", "Nicole", "Joe", "Obama", "Megan", "Alex", "Noah", "Liam", "Mason", "Jacob",
                  "William", "Ethan", "James", "Alexander", "Michael", "Benjamin", "Malcolm", "Mal", "Malcolm Reynolds",
                  "Zoe", "Zoe Washburne", "Kaylee", "Kaylee Fry", "Jayne","Jayne Cobb", "River", "River Tam", "Inara",
                  "Inara Serra", "Simon", "Simon Tam", "Shepherd Book", "Derrial Book", "Saffron", "Wash",
                  "Hoban Washburne", "Captain Kirk", "Commander Spock", "James T Kirk", "Spock", "Bones", "Leonard McCoy",
                  "Doctor McCoy", "Montgomery Scott", "Scotty", "Lt. Commander Scott", "Hikaru Sulu", "Sulu",
                  "Lt. Sulu", "Chekov", "Lt. Chekov", "Pavel Chekov", "Uhura", "Lt. Uhura", "Nyota Uhura",
                  "Nurse Chapel", "Christine Chapel", "the USS Enterprise", "the Enterprise"]

# list of firefly characters
firefly_character = ["Malcolm", "Mal", "Malcolm Reynolds", "Zoe", "Zoe Washburne", "Kaylee", "Kaylee Fry", "Jayne",
                     "Jayne Cobb", "River", "River Tam", "Inara", "Inara Serra", "Simon", "Simon Tam", "Shepherd Book",
                     "Derrial Book", "Saffron", "Wash", "Hoban Washburne"]




# list of series for the bot to draw from
st_series = ["Star Trek", "Star Trek: The Original Series"]


# list of plot-building events to make the tweet amusing
st_plot = ["contracts a disease that makes them speak exclusively in limericks", "technobabels",
           "finds the meaning of life", "initiates first contact with a strange planet",
           "gets their can opener stolen by gremlin", "gets ransomed for one cheese cracker",
           "enlists a small militia of raccoons", "is only able to eat spaghetti for rest of their life",
           "must peel every grape they encounter", "gets a strange looks from birds",
           "is only able to open water bottles upside down", "gets strange urge to follow the butterflies",
           "finds a door to a strange dimension but only once", "craves salt"]

# list of solutions to the strange plot
st_solution = ["has to bargain for a pair of ceremonial underpants", "has to kill it", "gets drunk", "dances it off",
               "has to lick it", "has to swear off cheese", "makes a grass crown", "fights a tree", "runs away",
               "cries", "dies", "can't die", "is willing to fight", "can't stop singing", "escapes", "can't escape",
               "kills a redshirt", "risks wear ing a red shirt", "falls in love"]





def create_tweet(series, character, plot, solution, verbs, nouns, syntax):
    """Create the text of the tweet you want to send."""

    if syntax == 1:
        # TWEET STRUCTURE
        # in this episode of <series> <character>
        # <plot> and <have to> <solution>

        random.seed()  # we're doing some randomization
        series_choice = random.randint(0, len(series) - 1)   # variable to choose which series to tweet
        character_choice = random.randint(0, len(character) - 1)  # variable to choose which character to tweet
        plot_choice = random.randint(0, len(st_plot) - 1)  # variable to choose which plot to tweet
        solution_choice = random.randint(0, len(st_solution) - 1)  # variable to choose which solution to tweet

        text = "In this episode of " + series[series_choice] + " " + character[character_choice] + " " + plot[plot_choice] + " and " + solution[solution_choice]
        return text

    if syntax == 2:
        # TWEET STRUCTURE
        # today <person> <plot>, <person> <solution>

        random.seed()  # we're doing some randomization
        character_choice1 = random.randint(0, len(character) - 1)  # variable to choose first character to tweet
        character_choice2 = random.randint(0, len(character) - 1)  # variable to choose second character to tweet
        plot_choice = random.randint(0, len(st_plot) - 1)  # variable to choose which plot to tweet
        solution_choice = random.randint(0, len(st_solution) - 1)  # variable to choose which solution to tweet

        text = "Today, " + character[character_choice1] + " " + plot[plot_choice] + ", " + character[character_choice2] + " " + solution[solution_choice]
        return text

    if syntax == 3:
        # TWEET STRUCTURE
        # the <noun> in <noun> <verb> in the <noun>

        random.seed()  # we're doing some randomization
        noun_choice1 = random.randint(0, len(nouns) - 1)  # variable to choose first noun to tweet
        noun_choice2 = random.randint(0, len(nouns) - 1)  # variable to choose second noun to tweet
        verb_choice = random.randint(0, len(verb) - 1)  # variable to choose which verb to tweet

        text = "I, a robot, made this tweet. #" + nouns[noun_choice1] + " #" + nouns[noun_choice2] + " #" + verbs[verb_choice]
        return text

    if syntax == 4:
        # TWEET STRUCTURE
        # <character> will <verb> the <noun>

        random.seed()  # we're doing some randomization
        character_choice = random.randint(0, len(character) - 1)  # variable to choose first noun to tweet
        noun_choice = random.randint(0, len(nouns) - 1)  # variable to choose second noun to tweet
        verb_choice = random.randint(0, len(verb) - 1)  # variable to choose which verb to tweet

        text = character[character_choice] + " will " + verbs[verb_choice] + " the " + nouns[noun_choice]
        return text


def tweet(text):
    """Send out the text as a tweet."""
    # Twitter authentication
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Send the tweet and log success or failure
    try:
        api.update_status(text)
    except tweepy.error.TweepError as e:
        log(e.message)
    else:
        log("Tweeted: " + text)


def log(message):
    """Log message to logfile."""
    path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    with open(os.path.join(path, logfile_name), 'a+') as f:
        t = strftime("%d %b %Y %H:%M:%S", gmtime())
        f.write("\n" + t + " " + message)



syntax_choice = 4


if __name__ == "__main__":
    if syntax_choice == 1:  # we want to make a Star Trek Episode
        tweet_text = create_tweet(st_series, st_character, st_plot, st_solution, verb, noun, syntax_choice)
        tweet(tweet_text)


    elif syntax_choice == 2:  # we want to make a lame news report
        tweet_text = create_tweet(st_series, rand_character, st_plot, st_solution, verb, noun, syntax_choice)
        tweet(tweet_text)


    elif syntax_choice == 3: # we want to become a self-aware twitter bot
        tweet_text = create_tweet(st_series, rand_character, st_plot, st_solution, verb, noun, syntax_choice)
        tweet(tweet_text)


    elif syntax_choice == 4: # we want a random character to do something weird
        tweet_text = create_tweet(st_series, rand_character, st_plot, st_solution, verb, noun, syntax_choice)
        tweet(tweet_text)
