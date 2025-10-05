# pylint: disable=line-too-long
"""
Spells can be cast as a ritual, reducing complexity by a factor of .75 per step and bypassing the casting power limit, but costing 1.25x the total power per step and taking significantly longer to cast (1 minute, 10 minutes, 1 hour, 6 hours, 24 hours, 1 week, 1 month, 6 months, 1 year).
Ritual casting cannot be used in combat or under duress. It is assumed that the ritual is performed in a safe, quiet environment with all necessary components and preparations made in advance.
If it takes more than 6 hours to cast a ritual, it is assumed that the caster regularly ties off the spellcasting process to rest and eat, resuming the ritual later. This does not incur additional time, complexity, or power costs. 

Spells consist of at least 1 of each of the following components:
- Delivery Method: How the spell travels before and sometimes after being activated.
- Target: The entity, item, or area the spell affects.
- Power Source: The origin of the spell's energy, such as a magical focus or innate ability.
- Variables: Additional parameters that can modify the spell's behavior or effects on-the-fly during casting.
- Trigger: The condition or event that causes the spell's payload to activate. Can be immediate, delayed, impact, conditional, or, at a significant cost, remotely activated/manipulated.
- Payload: The actual effect(s) of the spell. Can be multiple effects and can trigger/leverage other parts of the spell such as activating the delivery method again.

This module defines classes and enumerations to represent these components.

Notes:
- For simplicity, the first round of a spell's flight occurs during the round it is cast. All subsequent rounds of flight occur at the start of the caster's turn.
- A spell's activation occurs during the turn of the last round of travel unless otherwise specified.

- Base Cost: The initial flat cost of the spell component.
- Base Cost Multipliers: The multiplicative cost modifiers applied to the total cost of the spell due to the presence of this component.
    - These multipliers are applied multiplicatively to the combined base costs of the spell.
    - This represents the increased power requirement or difficulty in casting a spell with this component.
    - For example, a ranged spell would have to contain the magical energy during flight, increasing its complexity and power cost relative to a touch spell, and a very powerful spell would be more difficult to control, increasing its cost relative to a weaker spell.
- Cost per Range/Duration/Volume Unit: The additional linear cost incurred per unit of range/duration/volume.
    - This represents the increased power requirement or difficulty in casting a spell that travels further, lasts longer, or affects a larger area.
    - This is applied additively to the total cost of the spell. 
- 


The options and structure for each component are as follows:

Delivery Method:
- Instant Release: The spell is released instantly upon casting directly in front of you. No cost is applied as no containment is needed.
    - Base Cost: 0 Power, 0 Complexity
    - Base Cost Multipliers: 1 Power, 1 Complexity
    - Maximum Range: 5ft (immediately in front of caster)
    - Maximum Duration: 1 round (instantaneous)
    - Range Cost Multiplier: N/A
    - Duration Cost Multiplier: N/A
- Touch: The spell is placed upon touching a target and activates after a given duration. Requires physical contact and a Dex-based attack roll to successfully deliver the spell to an unwilling target.
    - Base Cost: 1 Power, 1 Complexity
    - Base Cost Multipliers: 1 Power, 1.1 Complexity
    - Maximum Range: Touch (5ft)
    - Maximum Duration: Up to 1 minute (10 rounds)
    - Range Cost Multiplier: x1 Power per 5ft per round
    - Duration Cost Multiplier: x1.25 Complexity per round after the first
- Ranged: The spell is launched towards a target within range. Requires line of sight and costs power based on distance per round. Requires a ranged spell attack roll to successfully hit an unwilling target.
    - Base Cost: 5 Power, 5 Complexity
    - Base Cost Multipliers: 1 Power, 1 Complexity
    - Maximum Range: Up to 100ft per level of the caster
    - Maximum Duration: Up to 1 minute (10 rounds).
    - Range Cost Multiplier: x(1 + 0.05 x distance) Power per 5ft per round.
    - Duration Cost Multiplier: x(1.5 ^ rounds) Complexity per round after the casting round. This is the maximum duration, but the spell can be set to activate earlier based on the trigger.
- Self: The spell affects only the caster. No cost is applied as no containment is needed.
    - Base Cost: 0 Power, 0 Complexity
    - Base Cost Multipliers: 1 Power, 1 Complexity
    - Maximum Range: Self (0ft)
    - Maximum Duration: Up to 1 minute (10 rounds)
    - Range Cost Multiplier: N/A
    - Duration Cost Multiplier: x1 Complexity per round after the first
- Enchant: The spell enchants an object or item to activate later. Generally requires a ritual to cast and significant preparation to create the enchanted item.
    - Base Cost: 2 Power, 2 Complexity
    - Base Cost Multipliers: 1 Power, 1 Complexity
    - Maximum Range: Touch (5ft)
    - Maximum Duration: Technically indefinite.
    - Range Cost Multiplier: N/A
    - Duration Cost Multiplier: x(1.1 ^ steps) Complexity per timeframe step after the first. Timeframe steps are as follows: 1 minute, 10 minutes, 1 hour, 6 hours, 24 hours, 1 week (5 days), 1 month (30 days), 6 months, 1 year.

Target:
- Target: The spell targets a specific creature or object.
- Multiple: The spell can target multiple creatures or objects. If targeting multiple entities, the spell's power cost is 2 ^ the number of targets over 1.
- Area: The spell affects a specific area.
    - Sphere: The spell affects a spherical area.
    - Cone: The spell affects a cone-shaped area in front of the activation point.
    - Line: The spell affects a straight line extending from the activation point.
    - Custom: The spell has a custom target type defined by the caster.
- Air Burst: The spell targets a point in space and affects an area around that point. This is generally used for 
"""


from enum import Enum


class DeliveryMethod:
    """How a spell travels before being activated. Multiple compatible delivery methods can be
    combined like ranged and touch to create a spell which attatches to a target and activates
    after a duration. Any type of delivery method except for instant release can retain its
    delivery method even after activating provided it retains sufficient power and has some
    mechanism to do so. An example of this would be an enchantment which activates it's effect
    after a duration but generally retains the enchantment for later reactivation."""
    def __init__(
            self,
            base_power_cost: float,
            base_complexity_cost: float,
            range_power_cost: float,
            duration_complexity_cost: float,
            complexity_cost_mult: float,
            power_cost_mult: float,
            description: str = ""
        ) -> None:
        """Initialize a DeliveryMethod instance. All multipliers are applied multiplicatively to
        the combined base costs of the spell. 

        Args:
            base_power_cost (float):
                The initial power cost associated with using this delivery method.
            base_complexity_cost (float):
                The initial complexity cost associated with using this delivery method.
            range_power_cost (float):
                The cost per 5ft per round of delivery speed.
            duration_complexity_cost (float):
                The cost per round of delivery duration.
            complexity_cost (float):
                The complexity cost multiplier associated with using this delivery method.
            power_cost (float):
                The initial power cost multiplier associated with using this delivery method.
            description (str, optional):
                A brief description of the delivery method. Defaults to "".
        """
        self.range_power_cost: float = range_power_cost
        self.duration_complexity_cost: float = duration_complexity_cost
        self.complexity_cost_mult: float = complexity_cost_mult
        self.power_cost_mult: float = power_cost_mult
        self.description: str = description


class Target:
    """Represents a target for a spell, whether it's a single entity, several, or an area."""
    def __init__(
            self,
            volume_power_cost: float,
            complexity_cost_mult: float,
            power_cost_mult: float,
            description: str = ""
        ) -> None:
        """Initialize a Target instance. All multipliers are applied multiplicatively to
        the combined base costs of the spell. 

        Args:
            volume_cost (float):
                The cost multiplier per unit of volume for the target.
            complexity_cost (float):
                The complexity cost multiplier associated with targeting this type.
            power_cost (float):
                The initial power cost multiplier associated with targeting this type.
            description (str, optional):
                A brief description of the target type. Defaults to "".
        """
        self.volume_power_cost: float = volume_power_cost
        self.complexity_cost_mult: float = complexity_cost_mult
        self.power_cost_mult: float = power_cost_mult
        self.description: str = description


class DeliveryMethodTypes(str, Enum):
    """Enumeration for different delivery methods of spells or abilities."""
    INSTANT_RELEASE = DeliveryMethod(
        base_power_cost=0, base_complexity_cost=0,
        range_power_cost=0, duration_complexity_cost=0,
        complexity_cost_mult=1, power_cost_mult=1,
        description="The spell is released instantly upon casting directly in front of you. \
            Effectively no delivery method with a range of 5ft and a duration of 1 round.")
    TOUCH = DeliveryMethod(
        base_power_cost=0, base_complexity_cost=1,
        range_power_cost=0, duration_complexity_cost=8,
        complexity_cost_mult=1.1, power_cost_mult=1,
        description="The spell is placed upon touching a target and activates after a given \
            duration.")
    RANGED = DeliveryMethod(
        base_power_cost=5, base_complexity_cost=5,
        range_power_cost=1, duration_complexity_cost=10,
        complexity_cost_mult=0, power_cost_mult=0,
        description="The spell is launched towards a target within range. Requires line of sight \
            and costs power based on distance per round.")
    SELF = DeliveryMethod(
        base_power_cost=0, base_complexity_cost=0,
        range_power_cost=0, duration_complexity_cost=0,
        complexity_cost_mult=0, power_cost_mult=0,
        description="The spell affects only the caster.")
    ENCHANT = DeliveryMethod(
        base_power_cost=0, base_complexity_cost=0,
        range_power_cost=0, duration_complexity_cost=0,
        complexity_cost_mult=0, power_cost_mult=0,
        description="The spell enchants an object or item to activate later.")

class TargetTypes(str, Enum):
    """Enumeration for different target types of spells or abilities."""
    TARGET = Target(volume_power_cost=0, complexity_cost_mult=1.5, power_cost_mult=1, description="The spell targets a specific creature or object.")
    SPHERE = Target(volume_power_cost=1, complexity_cost_mult=1, power_cost_mult=2, description="The spell affects a spherical area.")
    CONE = Target(volume_power_cost=1, complexity_cost_mult=1.25, power_cost_mult=1.5, description="The spell affects a cone-shaped area in front of the activation point.")
    LINE = Target(volume_power_cost=1, complexity_cost_mult=1.25, power_cost_mult=1.25, description="The spell affects a straight line extending from the activation point.")

class Spell:
    def __init__(self, name: str, description: str, delivery_method: DeliveryMethodTypes) -> None:
        self.name: str = name
        self.description: str = description
        self.delivery_method: DeliveryMethodTypes = delivery_method
