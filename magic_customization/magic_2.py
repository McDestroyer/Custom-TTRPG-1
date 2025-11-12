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
- Elemental Components V2
    # Manipulates the elements for damage or utility. Each effect requires some of its element to be present to manipulate, with thermal and electrical effects transferring energies to operate without direct elemental presence.
    - Air
        # Manipulates air for utility, defense, or minor damage. Requires air to be present to function.
        - Wind
            # Manipulates wind currents to create powerful gusts or calming breezes. Depending on the strength can enflame or extinguish fires or propel objects.
            # Can also be used for flight or enhanced jumping.
        - Deflective Barrier
            # Creates a barrier of swirling air that has a chance to deflect some projectiles or reduce overall damage by choosing hit locations when out of hitpoints. Does nothing against melee attacks, but cannot be physically broken, only dispelled.
        - Sound Manipulation
            # Manipulates sound waves to create deafening blasts or silent zones. Can be used to obscure sounds or enhance them. Can deal minor sonic damage and restrict the usage of verbal components.
        - Air Pressure Manipulation
            # Manipulates air pressure to suffocate targets or enhance breathing in low-oxygen environments. Combined with a solid barrier can maintain a survivable atmosphere in vaccum or high-pressure environments.
            # Creates a shockwave of compressed air that can knock back targets and objects if released from a contained space suddenly.
        - Air Solidification
            # Solidifies air to create temporary platforms, barriers, tools, or weapons. Can only make simple shapes like walls, swords, and other non-mechanically complex objects. Sucks in surrounding air to create the solid forms and costs mana to upkeep.
            # The solidified air objects are fragile and can be broken with enough force. Note that solidified air objects still require support from the ground or other objects to maintain their position unless otherwise levitated by force or wind manipulation.
    - Earth
        # Manipulates earth for damage, utility, or defense. Requires earth to be present to function. Counteracts lightning effects.
        - Earthen Creation
            # Manipulates stone and rock to create barriers, weapons, or projectiles. Can also be used to reshape terrain or create simple structures.
        - Magnetism
            # Manipulates metal objects, allowing the caster to attract or repel them. Can also be used to disarm opponents (DC dependant on the strength of the magnetism) or stick metal objects together.
        - Earthen Barrier
            # Creates a barrier of earth that provides cover and can absorb damage instead of the caster. The barrier can be shaped to the caster's will but cannot be made into complex shapes or mechanisms.
            # The barrier can be destroyed with enough damage or dispelled. upon being dispelled, the earth maintains its original form and position, simply returning to normal earth/stone, potentially trapping anything within it. Breathable air is limited within the barrier based on its size.
        - Earthquake
            # Creates localized tremors that can knock down targets and destabilize structures. The intensity can vary from minor shakes to significant quakes based on mana input.
        - Burrowing
            # Allows the caster to tunnel through earth and stone, creating passages or hiding places. The speed and size of the tunnel depend on the caster's skill. Cannot tunnel through metal or magically reinforced materials.
            # Note that earth tunneling can cause cave-ins or destabilize structures if not done carefully and material is never created or destroyed, only moved.
        - Earth Spike
            # Creates spikes of earth that impale targets at range on the condition that the target is in contact with the earth, dealing damage and potentially causing bleeding. The spikes can be shaped and sized based on the caster's intent.
            # The spikes can be created in various sizes and shapes, from small, sharp points that can cause bleeding to large, bludgeoning masses which can bypass some armors.
        - Oil Spray
            # Creates a spray of oil from earth-based materials that can create slippery surfaces or be ignited for fire-based effects. The oil can be manipulated to cover specific areas or targets. Adds a DC to movement and dexterity-based checks within the affected area and gives an advantage to escaping grappling when affected.
            # Remains on surfaces until cleaned, burned, manipulated, or absorbed into the earth again.
    - Fire
        # Manipulates fire and heat for damage, utility, or defense. Can operate without direct fire presence by converting thermal energy but requires a spark or flame for fire attacks. Consumes breathable air at a rate dependent on the size of the fire created. Counteracts cold and water effects.
        - Flame Creation
            # Creates and shapes flames for various effects, such as igniting objects, creating light sources, or forming weapons. The intensity and size of the flames can be controlled by the caster. Holding or touching a purely fire-based flame weapon without proper protection is not recommended.
        - Heat Manipulation
            # Manipulates thermal energy to heat objects or areas, potentially causing burns or igniting flammable materials. Can also be used to warm objects or allies, cause similar effects to heat metal,
            # purify water by boiling it, melt ice, create thermal updrafts for flight assistance, or ignite objects if heated to sufficient temperatures.
        - Fire Barrier
            # Creates a barrier of flames that damages anyone who passes through it. The barrier can be shaped and sized based on the caster's intent.
            # The barrier can be extinguished with enough water or dispelled. upon being dispelled, the fire dissipates when the spell does. The barrier provides light in dark areas.
        - Explosion
            # Creates a fiery explosion that deals area damage. The size and intensity of the explosion can vary based on mana input.
        - Flame Thrower
            # Projects a beam of fire that can engulf targets in flames, dealing damage to all in its path. The length and width of the flame can be adjusted by the caster.
        - Cauterization
            # Closes wounds by burning them shut, dealing a small amount of fire damage but preventing further bleeding and infection. Can also be used to seal objects or surfaces.
            # Can be used in emergency situations to stop bleeding quickly, though it causes pain and minor burns.
    - Water
        # Manipulates water for utility, defense, or minor damage. Requires water to be present to function. Generally used for pushing, pulling, drowning, and restraining effects rather than direct damage. Counteracts fire and heat effects, but amplifies lightning and cold effects.
        - Water Shaping
            # Manipulates water to create barriers, weapons, or projectiles. Can also be used to reshape terrain or create simple structures.
        - Drenching
            # Soaks a target or area with water, extinguishing flames and making surfaces slippery. Can also be used to hydrate plants or cool overheated objects.
        - Water Barrier
            # Creates a barrier of water that reduces incoming damage and can extinguish flames and ground lightning. The barrier can be shaped to the caster's will but cannot be made into complex shapes or mechanisms.
            # The barrier cannot be destroyed with physical damage but can be dispelled. Upon being dispelled, the water dissipates when the spell does.
        - Tidal Wave
            # Creates a massive wave of water that crashes down on targets, dealing damage and potentially knocking them prone. The size and intensity of the wave can vary based on mana input.
        - Water Jet
            # Creates a high-pressure jet of water that deals minor damage and can push targets away. The pressure and range of the jet can be adjusted by the caster.
        - Healing Waters
            # Heals targets within a body of water over time. The healing effect is enhanced by the purity of the water used.
        - Tidal Pull
            # Manipulates water currents to pull targets towards a specific point, potentially dragging them underwater if they are in a body of water. The strength of the pull can be adjusted by the caster.
    - Lightning
        # Manipulates electricity for damage, utility, or defense. Can operate without direct lightning presence by converting electrical energy from nearby sources. Lightning effect amplified if the target is wet but is counteracted by earth effects.
        - Static Shock
            # Generates static electricity on your body, dealing minor lightning damage to attackers who hit you with melee attacks. The intensity of the shock can be adjusted by the caster.
        - Lightning Bolt
            # Calls down a bolt of lightning from the sky, dealing heavy damage to a target. The bolt's size and intensity can be increased by expending more mana.
        - Chain Lightning
            # Releases a bolt of lightning that arcs between multiple targets, dealing damage to each. The number of targets and the intensity of the lightning can be adjusted by the caster.
        - Overcharge
            # Increases the power of your next lightning spell, allowing it to deal extra damage or have additional effects. The amount of overcharge can be controlled by the caster.
            # Overcharge can be stacked, but each stack increases the risk of backlash.
        - Stun
            # Releases a burst of electrical energy that stuns targets in an area. The size of the area and duration of the stun can be adjusted by the caster.
    - Cold
        # Manipulates ice and cold for damage, utility, or defense. Requires water or moisture to be present to function. Counteracts fire and heat effects, but amplified if the target is wet.
        - Frostbite
            # Deals cold damage to a target and reduces their movement speed. The severity of the frostbite can be adjusted by the caster.
        - Ice Barrier
            # Creates a weak barrier of ice that absorbs incoming damage until destroyed by freezing a water barrier. The barrier's size and thickness can be adjusted by the caster.
        - Blizzard
            # Summons a storm of ice and snow that deals damage and obscures vision in the area. The intensity and duration of the blizzard can be controlled by the caster.
        - Freeze
            # Freezes a target or area, causing ongoing cold damage and potentially immobilizing them. The size and duration of the freeze can be adjusted by the caster.
        - Frostburn
            # Creates a beam of freezing energy that damages and slows targets in a line. The size and intensity of the beam can be adjusted by the caster.
- Elemental combinations (e.g., Steam, Mud, Lava, Ice Storm, etc.)
    # Combines two or more elements to create unique effects that leverage the properties of each element.
    - Water + Cold
        - Ice Shard Field
            # Combines water and cold elements to create a field of sharp ice shards that damage and slow targets.
        - Ice Wall
            # Combines water and cold elements to create a wall of ice that provides cover and can freeze attackers.
        - Ice Weapon
            # Combines water and cold elements to create a weapon made of ice that deals cold damage and can freeze targets.
    - Water + Lightning
        - Electrified Water
            # Combines water and lightning elements to create electrified water that deals lightning damage to anyone in contact with it.
        - Thunderous Wave
            # Combines water and lightning elements to create a wave of water infused with lightning that deals damage and can stun targets.
    - Fire + Air
        - Firestorm
            # Combines fire and air elements to create a storm of fire that deals damage and obscures vision.
        - Smoke Screen
            # Combines fire and air elements to create a thick smoke that obscures vision.
    - Steam
        # Combines water and fire elements to create scalding steam that damages and obscures vision.
    - Mud
        # Combines earth and water elements to create a sticky mud that hinders movement and visibility.
    - Lava
        # Combines earth and fire elements to create a flow of lava that deals damage over time and creates hazardous terrain.
    - Ice Storm
        # Combines water and air elements to create a storm of ice shards that deals damage and slows targets.
- Creation
    # Creates objects or constructs from magical energy or raw materials. Can not replicate enchantments or magical properties directly, but can create objects that can be enchanted later.
    - Emulation
        # Creates objects by making them out of magical energy that mimics the properties of real materials. The created objects are temporary and dissipate after a certain duration or when dispelled.
        - Basic Emulation
            # Creates simple objects like tools, weapons, or barriers out of what apppears to be a single material (wood, stone, metal, etc.) with basic functionality.
        - Standard Emulation
            # Creates more complex objects with enhanced functionality and durability, such as mechanical devices, out of multiple materials, such as wood and metal combined into a shovel.
        - Advanced Emulation
            # Creates highly advanced objects with intricate designs and superior performance, often indistinguishable from the real thing. Materials can be combined in more complicated ways, such as mixtures or alloys in complicated devices.
        - Master Emulation
            # Creates objects that are near perfect replicas of real materials, including their properties and behaviors. These objects are almost indistinguishable from the real thing and can be used in any situation where the original material would be used.
            # Can create living constructs that mimic the behavior of real creatures, such as golems or animated objects.
        - True Emulation
            # Creates objects that are perfect replicas of real materials, including their properties and behaviors. These objects are indistinguishable from the real thing and can be used in any situation where the original material would be used.
            # Can emulate living creatures with high fidelity, including their behaviors and abilities, effectively creating lifelike constructs.
    - Materialization
        # Creates solid objects from raw magical energy, allowing for permanent constructs without an upkeep but a massive initial cost.
        # The complexity and durability of the created objects depend on the caster's skill and the amount of magical energy used. Identical to Emulation in terms of effect tiers, but the objects created are permanent and the complexity and power requirements are much higher.
- Destruction
    # Destroys objects or constructs by breaking down their magical or physical structure. Can not directly destroy magical properties or enchantments, but can destroy the object they are attached to.
    - Disintegration
        # Breaks down objects into their basic components, effectively destroying them. The infused mana and durability of the object determine how difficult it is to disintegrate. Does not work on living creatures or significantly imbued objects.
    - Dispel Construction
        # Removes magical energy from constructs or enchanted objects, effectively destroying them. The strength of the enchantment or construct determines how difficult it is to dispel. Can work on living constructs but not on living creatures.
- Transformation
    # Alters the form or properties of objects or creatures. Can not replicate enchantments or magical properties directly, but can change the physical form of the target.
    - Polymorph
        # Changes the form of a target into another creature or object. The complexity and duration of the transformation depend on the caster's skill and the amount of magical energy used. The target can resist the transformation based on their own magical resilience.
    - Transmute
        # Alters the physical properties of a target, such as changing metal into wood or stone into glass. The complexity and duration of the transmutation depend on the caster's skill and the amount of magical energy used. The target can resist the transmutation based on their own magical resilience.
    - Enhance/Reduce
        # Increases or decreases the size, strength, or other attributes of a target. The complexity and duration of the enhancement or reduction depend on the caster's skill and the amount of magical energy used. The target can resist the effect based on their own magical resilience.
- Information
    # Stores, retrieves, or manipulates information through magical means.
    - Information Storage
        # Stores information such as a message, image, or sound in a magical medium for later retrieval.
    - 
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