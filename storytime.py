from random import randint
import copy
story = (
    "A vacation is when you take a trip to some {} place with your {} family." +
    " Usually you go to some place that is near a/an {} or up on a/an {}." +
    " A good vacation place is one where you can ride {} or play {} or go hunting for {}." +
    " I like to spend my time {}." +
    " When parents go on vacation, they spend their time eating three {} a day, and fathers go fishing, and mothers sit around {}." +
    " Last summer, my little brother fell in a/an {} and got poison {} all over his {}." +
    " My family is going to go to the {}, and I will practice {}." +
    " Parents need vacations more than kids because parents are always very {} and because they have to work {} hours a day all year long making enough {} to pay for the vacation!"
)

#create a dictionary to lookup words by type
word_dict = {
    'adjective':['godawful','sinister','abnormal','useless','fear-inspiring'],
    'adjective':['zombie-like','territorial','magical','greedy','frozen'],
    'noun':['sound-barrier', 'cheap natural history', 'haunted graveyard','mad cow disease','laptop'],
    'noun':['backstabbing misfortune', 'old irish cottage', 'reading party', 'volcanic crater','dragon tail'],
    'plural noun':['lobsters','hippos','coffee pots','whales','cats'],
    'game':['human pinata','poop squisher','knife juggling','bloody mary','pin the tail on mom'],
    'plural noun':['witches','boxes','hearts','skulls','corn'],
    'verb ending in -ing':['eating','irritating','crying','yelling','sleeping'],
    'plural noun':['humans','aliens','cockroaches','hyenas','frogs'],
    'verb ending in -ing':['pooping','shopping','couponing','packing','grounding'],
    'noun':['toilet seat','mad cow disease','weed whacker','electric furnace','hot volcano'],
    'plant':['mushrooms', 'acorns','sunflower','ivy','mint'],
    'part of the body':['butt','armpit','adams apple','toe','groin'],
    'a place':['movie rental store','florist','deli','ice cream shop','bank'],
    'verb ending in -ing':['ice skating','dungeons and dragons','farting','burping','bowling'],
    'adjective':['stressed','violent','demanding','stubborn','abnormal'],
    'number':['3','10','5','6','9'],
    'plural noun':['corrupt broken promises','travel guidebooks', 'french fries','heartbreaks','deer antlers'],
    
}

def get_word(type, local_dict):
    words = local_dict[type]
    cnt = len(words)-1
    index = randint(0, cnt)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective', local_dict),
        get_word('adjective', local_dict),
        get_word('noun', local_dict),
        get_word('noun', local_dict),
        get_word('plural noun', local_dict),
        get_word('game', local_dict),
        get_word('plural noun', local_dict),
        get_word('verb ending in -ing', local_dict),
        get_word('plural noun', local_dict),
        get_word('verb ending in -ing', local_dict),
        get_word('noun', local_dict),
        get_word('plant', local_dict),
        get_word('part of the body', local_dict),
        get_word('a place', local_dict),
        get_word('verb ending in -ing', local_dict),
        get_word('adjective', local_dict),
        get_word('number', local_dict),
        get_word('plural noun', local_dict)
    )

print("STORY 1: ")
print(create_story())
print()
print("STORY 2: ")
print(create_story())




