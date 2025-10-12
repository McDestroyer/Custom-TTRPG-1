"""
Payload Components are the effects that a spell has when cast. They have mana, complexity, and time costs associated with them.

Mana cost is the amount of magical energy required to use the component. This cost can vary based on the strength and number of effects included in the component.
Cost of the spell is summed up and consumed each round the spell is active.

Complexity is determined by the number and type of effects, as well as any additional factors such as the spell's level or the caster's skill.

Time is the duration the component takes to manifest its effects. Some effects are instantaneous, while others may have a duration or be ongoing.
Some effects may also have a cooldown period before they can be used again.


Projectile spells with impact triggers require an attack roll to hit the target. The attack roll is made using the caster's spellcasting ability modifier and proficiency bonus (if applicable).
If the attack hits, the spell's effects are applied to the target. If the attack misses, the spell may still have secondary effects or may simply fail to affect the target.

Touch spells require the caster to be within 5 feet of the target. The caster must use their action to touch the target and deliver the spell's effects. If the target is unwilling, they can make a Dexterity saving throw to avoid being touched.

Area spells affect all creatures and objects within a specified area. The caster must choose the center point of the area and all creatures and objects within that area are affected by the spell's effects. Creatures can make a Dexterity saving throw to avoid or reduce the effects of the spell.


Payload Component Categories:
- Damage
    # Deals damage to or heals whatever is in the spell's area of effect based on the element chosen.
    - Physical
        - Bludgeoning
        - Piercing
        - Slashing
    - Magical
        - Fire
        - Ice
        - Lightning
        - Acid
        - Poison
        - Force
- Life/Anti-Life
    # Affects the health of 1 or more creatures.
    - Direct
        # Heals or damages the target instantly.
        - Life
        - Anti-Life
    - Transfer
        # Transfers health from one target to another. Can be resisted. This is considered either Life or Anti-Life damage. Requires two targets.
    - Absorb
        # Absorbs health from a target and turns it into mana. This is considered either Life or Anti-Life damage.
    - Drain
        # Drains health from a target over time. This is considered either Life or Anti-Life damage. Can be resisted.
- Buff/Debuff
    # Affects the attributes or abilities of 1 or more creatures.
    - Attribute
        # Increases or decreases a specific attribute (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma) of the target.
    - Ability
        # Increases or decreases a specific ability (Attack, Defense, Speed, etc.) of the target.
    - Status
        # Applies a status effect (Stunned, Poisoned, etc.) to the target.
- Summon
    # Summons a creature or object to aid the caster. The summoned entity has its own stats and abilities.
    - Creature
        # Summons a creature to fight for the caster. The creature has its own stats and abilities.
    - Object
        # Summons an object to aid the caster. The object has its own properties and abilities.
- Mind
    # Affects the mind of 1 or more creatures.
    - Control
        # Takes control of a target's actions for a short period of time. The target can resist this effect.
    - Influence
        # Influences a target's thoughts or emotions. The target can resist this effect.
    - Illusion
        # Creates an illusion that affects the senses of the target. The target can resist this effect.
    - Damage
        # Deals psychic damage to the target, affecting their mental state.
- Radiance
    # Affects light and radiant energy for illusion, damage, or utility.
    - Light Manipulation
        # Creates, shapes, or manipulates light for various effects (blinding, illuminating, illusion, etc.).
    - Sound Manipulation
        # Creates, shapes, or manipulates sound for various effects (deafening, communication, illusion, etc.).
    - Radiant Damage
        # Deals radiant damage to targets, effective against undead and dark-aligned creatures.
    - Thunder Damage
        # Deals thunder damage, causing concussive force and potential deafness.
- Time
    # Affects the flow of time for 1 or more creatures or objects.
    - Acceleration
        # Speeds up the target's actions or the flow of time in a specific area.
    - Deceleration
        # Slows down the target's actions or the flow of time in a specific area.
    - Temporal Shift
        # Shifts the target forward or backward in time for a short period.
    - Time Reversal
        # Rewinds time for the target, undoing recent actions or effects.
    - Time Stop
        # Stops time for everyone except the caster, allowing them to act freely for a short period.
# TODO: Make this more modular and less hardcoded.
- Elemental
    # Manipulates the elements for damage or utility.
    - Fire
        # Deals heat damage to targets, igniting them and causing ongoing burn damage.
        - Heat
            # Generates heat to scorch or melt objects and surfaces or to warm objects or allies. Can also be used to purify water. (Similar to Heat Metal)
        - Flame
            # Creates a fire in a shape or area that damages. Can also be used to light objects or provide warmth. (Similar to Produce Flame or Flame Blade)
        - Explosion
            # Creates a fiery explosion that deals area damage and ignites the surroundings. (Similar to Fireball or Burning Hands)
        - Ember
            # Creates a small, glowing ember that can ignite flammable objects. (Similar to Prestidigitation)
        - Ignite
            # Ignites a target or area, causing ongoing fire damage.
        - Smoke
            # Creates a cloud of smoke that obscures vision and can choke or blind creatures. (Similar to Fog Cloud)
        - Flash
            # Creates a bright flash of light that can blind creatures. (Similar to Flashbang or Daylight)
        - Cauterization
            # Closes wounds by burning them shut, dealing a small amount of damage but preventing further bleeding and infection. Can also be used to seal objects or surfaces. (Similar to a more intense version of Heat)
        - Purification
            # Removes toxins, diseases, or curses from a target. Can also be used to purify food and water. (Similar to Lesser Restoration or Purify Food and Drink)
        
    - Ice
        # Deals cold, slashing, or piercing damage to targets, freezing them and potentially slowing their movements.
        - Hypothermia
            # Deals cold damage and reduces the target's speed. (Similar to Ray of Frost)
        - Ice Shard
            # Creates a shard of ice that slices or impales the target, dealing damage and potentially causing bleeding. (Similar to Ice Knife)
        - Snowstorm
            # Creates an AoE storm of snow and ice that obscures vision and slows movement. (Similar to Sleet Storm)
        - Freeze
            # Freezes a target or area, causing ongoing cold damage and potentially immobilizing them.
        - Ice Field
            # Creates a field of ice that makes the ground slippery and difficult to traverse. (Similar to Grease but with ice)
        - Ice Barrier
            # Creates a barrier of ice that absorbs damage and can freeze attackers. (Similar to Shield)
        - Ice Prison
            # Traps a target in a cage of ice, immobilizing them and dealing ongoing cold damage. (Similar to Hold Person but with ice)
        - Hail
            # Creates a storm of hail that deals damage to targets in an area. (Similar to Call Lightning but with hail)
        - Shattered Field
            # Creates a field of ice that shatters when stepped on, dealing damage to those who move through it.
        - Frostbite
            # Deals cold damage and gives vulnerability to physical damage. (Similar to Frostbite cantrip)
    - Lightning
        # Deals lightning damage to targets, shocking them and potentially causing paralysis. Can be used to explode or electrify objects.
        - Shock
            # Deals lightning damage and has a chance to stun the target. (Similar to Shocking Grasp)
        - Chain Lightning
            # Creates a bolt of lightning that arcs between multiple targets, dealing damage to each. (Similar to Chain Lightning spell)
        - Thunderstorm
            # Creates a storm of lightning and thunder in an area, dealing damage and potentially stunning targets. (Similar to Call Lightning but with thunder)
        - Static Charge
            # Charges the target with static electricity, causing damage to attackers who hit them with melee attacks. (Similar to the spell Armor of Agathys but with lightning)
        - Lightning Strike
            # Calls down a bolt of lightning to strike a target, dealing heavy damage and area thunder damage. (Similar to Call Lightning)
        - Overcharge
            # Overcharges a target with electricity, causing ongoing lightning damage and potentially stunning them. (Similar to a more intense version of Shock)
        - Electrocute
            # Deals heavy lightning damage to a target and has a chance to paralyze them. (Similar to a more powerful version of Shock)
        - Thunderclap
            # Creates a loud clap of thunder that damages and deafens targets in an area. (Similar to Thunderwave)
        - Electrolosis
            # Converts water into either breathable or explosive gas using electricity.
    - Water
        # Deals physical damage to targets, potentially drenching them and causing vulnerability to Ice and Lightning damage. Primarily area control and utility.
        - Drench
            # Soaks a target or area with water, extinguishing flames and making surfaces slippery. (Similar to Create or Destroy Water)
        - Water Jet
            # Creates a high-pressure jet of water that deals damage and can push targets away. (Similar to Eldritch Blast but with water)
        - Tidal Wave
            # Creates a massive wave of water that crashes down on targets, dealing damage and potentially knocking them prone. (Similar to the spell Tidal Wave)
        - Water Shield
            # Creates a shield of water that absorbs damage and can extinguish flames. (Similar to Shield but with water)
        - Whirlpool
            # Creates a swirling vortex of water that pulls in and restrains targets. (Similar to the spell Hold Person but with water)
        - Water Breathing
            # Allows the target to breathe underwater for a duration. (Similar to the spell Water Breathing)
        - Flood
            # Creates a localized flood that affects an area, making it difficult terrain and potentially sweeping away targets. (Similar to the spell Control Water)
        - Mist
            # Creates a thick mist that obscures vision and can cause confusion. (Similar to the spell Fog Cloud)
        - Healing Waters
            # Heals targets within a body of water over time. (Similar to the spell Healing Spirit but with water)
        - Surface Tension
            # Adjusts the surface tension of water to create a solid platform or trap.
        - Current
            # Creates a strong current in a body of water that can push or pull targets. (Similar to the spell Control Water)
        - Cleanse
            # Cleanses toxins, diseases, or curses from a target using water. (Similar to Lesser Restoration but with water)
        - Purify
            # Purifies a body of water, removing impurities and toxins. (Similar to the spell Purify Food and Drink but with water)
        - Condensation
            # Condenses moisture in the air to create water, fog, or ice. (Similar to Create or Destroy Water but with more versatility)
        - Water Blade
            # Creates a blade of water that can slice through targets. (Similar to the spell Blade Barrier but with water)
        - Water Prison
            # Traps a target in a sphere of water, immobilizing them and potentially drowning them. (Similar to the spell Hold Person but with water)
    - Earth
        # Deals physical damage to targets, potentially causing them to become entangled or immobilized.
        - Quake
            # Creates a localized earthquake that damages and knocks down targets. (Similar to the spell Earthquake)
        - Stone Skin
            # Turns the target's skin to stone, increasing their defense but reducing their speed. (Similar to the spell Stoneskin)
        - Earth Spike
            # Creates spikes of earth that impale targets, dealing damage and potentially causing bleeding. (Similar to the spell Spike Growth)
        - Mudslide
            # Creates a slide of mud that knocks down and restrains targets. (Similar to the spell Entangle)
        - Sandstorm
            # Creates a storm of sand that obscures vision and damages targets. (Similar to the spell Dust Devil)
        - Earth Wall
            # Creates a wall of earth that provides cover and can block movement. (Similar to the spell Wall of Stone)
        - Tremor
            # Creates a shockwave that damages and potentially knocks down targets in a cone. (Similar to the spell Earth Tremor)
        - Petrify
            # Turns a target to stone, immobilizing them and making them immune to damage. (Similar to the spell Flesh to Stone)
        - Burrow
            # Allows the caster to tunnel through the earth, creating a passage or hiding place. (Similar to the spell Burrow)
        - Entomb
            # Encases a target in earth, immobilizing them and dealing damage over time. (Similar to the spell Earthbind but more intense)
        - Sinkhole
            # Creates a sudden pit in the ground that can swallow targets. (Similar to the spell Sinkhole)
        - Oil Slick
            # Creates a slick surface that causes targets to slip and fall. (Similar to the spell Grease but with oil)
        - Greased Pig
            # Covers a target in grease, making them difficult to grapple and increases their movement speed/Dodge. (Similar to the spell Grease)
        - Avalanche
            # Causes a mass of earth and rock to fall on targets, dealing damage and potentially burying them. (Similar to the spell Avalanche)
        - Catapult
            # Hurls a target through the air, dealing damage and potentially knocking them prone. (Similar to the spell Catapult)
        - Projectile
            # Hurls a rock or chunk of earth at a target, dealing damage. (Similar to the spell Magic Stone)
        - Earth Shield
            # Creates a barrier of earth that absorbs damage. (Similar to the spell Shield)
        - Magnetism
            # Manipulates metal objects, allowing the caster to attract or repel them. Can also be used to disarm opponents. (Similar to the spell Mage Hand but with metal)
        - Magnetize
            # Magnetizes a target or area, attracting or repelling metal objects. Can also be used to disarm opponents. (Similar to the spell Mage Hand but with metal)
        - Iron Grip
            # Increases the target's grip strength, allowing them to hold onto objects or resist being disarmed. (Similar to the spell Enhance Ability but with a focus on grip strength)
        - Iron Fist
            # Enhances the target's unarmed strikes with metal, increasing damage and potentially causing bleeding. (Similar to the spell Magic Weapon but with metal)
        - Crush
            # Crushes a target with immense pressure, dealing heavy damage and potentially stunning them. (Similar to the spell Enervation but with physical crushing force)
        - Corrosion
            # Corrodes metal objects, weakening them and potentially causing them to break. Can also be used to damage metal armor or weapons. (Similar to the spell Acid Splash but with a focus on metal)
        - Metal Shards
            # Creates a barrage of sharp metal shards that deal damage and can cause bleeding. (Similar to the spell Shard but with metal)
    - Air
        # Deals slashing damage to targets, potentially pushing them away or causing disorientation. Primarily used for mobility and deflection of projectiles.
        - Gust
            # Creates a strong gust of wind that pushes targets away and can extinguish flames. (Similar to the spell Gust of Wind)
        - Air Shield
            # Creates a shield of air that deflects projectiles and absorbs damage. (Similar to the spell Shield but with air)
        - Tornado
            # Creates a powerful tornado that sweeps away targets and debris. (Similar to the spell Wind Wall but with more destructive potential)
        - Levitate
            # Allows the target to levitate off the ground, gaining increased mobility and the ability to avoid ground-based hazards. (Similar to the spell Levitate)
        - Air Solidification
            # Solidifies air to create temporary platforms or barriers. (Similar to the spell Wall of Force but with air)
        - Vacuum
            # Creates a vacuum that sucks in air and objects, potentially suffocating targets. (Similar to the spell Vacuum but more intense)
        - Wind Blade
            # Creates a blade of compressed air that slices through targets. (Similar to the spell Blade Barrier but with air)
        - Air Slash
            # Creates a slashing wave of air that damages and disorients targets. (Similar to the spell Slashing Wave but with air)
        - Cyclone
            # Creates a swirling cyclone of air that damages and disorients targets. (Similar to the spell Whirlwind)
- Creation
- Destruction
- Environmental
- Transformation
- Information
- Controlflow
- Space
- Soul
- Spellcraft
"""
# Overheal: Possible effects include slowness, vulnerability to certain damage types, 

# class EffectTypes:
#     DAMAGE = "damage"
#     HEAL = "heal"
#     BUFF = "buff"
#     DEBUFF = "debuff"
#     SUMMON = "summon"
#     SHIELD = "shield"
#     CONTROL = "controlflow"
#     ENVIRONMENTAL = "environmental"


class Spell:
    def __init__(self, name, container, propulsion, trigger, power_source, senses, variables, payload):
        self.name = name
        self.container = container
        self.propulsion = propulsion
        self.trigger = trigger
        self.power_source = power_source
        self.senses = senses
        self.variables = variables
        self.payload = payload

    def cast(self, *variables):
        return f"Casting {self.name} and variables {variables}!"

    # TODO: Calculate complexity based on spell attributes.
    @property
    def complexity(self) -> int:
        return 0

    # TODO: Calculate initial mana cost based on spell attributes.
    @property
    def initial_mana_cost(self) -> int:
        return 0


class Payload:
    def __init__(self, effects: list[PayloadItem]):
        self.effects = effects

    def apply(self, target):
        return f"Applying {self.effects} to {target}."

class PayloadItem:
    def __init__(self, effect_type: str, magnitude: int, duration: int) -> None:
        self.effect_type = effect_type
        self.magnitude = magnitude
        self.duration = duration

    def __repr__(self) -> str:
        return f"{self.effect_type} (Magnitude: {self.magnitude}, Duration: {self.duration})"