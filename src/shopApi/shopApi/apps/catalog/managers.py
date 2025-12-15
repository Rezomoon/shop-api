from treebeard.mp_tree import MP_NodeQuerySet

# Dar inja etefaghate moshtarak ye masalan Query haye moshtarak ra negah midarim ta dar zamane taghir faghat haminja avazeshoon konim !


# Baraye mesal ma bayad etelaate mahsolatemaan ra baraye samte shop va user va front faghat 
# Mahsolate is_public = true ro befrestim Yani hich fargh dige iyee nmikonad 
# Pas chon  hame ja in qazie emal mishavad bayad jodaganeh dashte bashimesh 

class CategoryQuerySet(MP_NodeQuerySet) :
    def public(self):
        return self.filter(is_public = True)
