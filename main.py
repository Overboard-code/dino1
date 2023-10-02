namespace SpriteKind {
    export const boss = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.boss, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprites.destroy(projectile)
    boss_hleth += -1
    animation.runImageAnimation(
    mySprite4,
    [],
    100,
    false
    )
    pause(5000)
    animation.runImageAnimation(
    mySprite4,
    [],
    100,
    false
    )
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (info.score() >= 3) {
        mySprite4 = sprites.create(, SpriteKind.boss)
        mySprite4.setPosition(146, 51)
        mySprite4.changeScale(2, ScaleAnchor.Middle)
        dave += 1
        boss_hleth = 10
        scene.setBackgroundImage()
        animation.stopAnimation(animation.AnimationTypes.All, mySprite)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    pauseUntil(() => dave == 1)
    animation.runImageAnimation(
    mySprite,
    [],
    200,
    false
    )
    pause(500)
    projectile = sprites.createProjectileFromSprite(, mySprite, 100, 0)
    animation.runImageAnimation(
    projectile,
    [],
    500,
    false
    )
    pause(1000)
    animation.runImageAnimation(
    mySprite,
    [],
    500,
    false
    )
})
sprites.onOverlap(SpriteKind.Food, SpriteKind.Enemy, function (sprite, otherSprite) {
    mySprite3.setVelocity(-50, 0)
    mySprite2.setVelocity(-50, 0)
    mySprite3.setPosition(153, randint(10, 111))
    mySprite2.setPosition(153, randint(10, 111))
})
info.onLifeZero(function () {
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    info.changeScoreBy(1)
    sprites.destroy(mySprite2)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(mySprite3)
    info.changeLifeBy(-1)
})
let projectile2 = 0
let mySprite5: Sprite = null
let mySprite2: Sprite = null
let mySprite3: Sprite = null
let mySprite4: Sprite = null
let projectile: Sprite = null
let dave = 0
let boss_hleth = 0
let mySprite: Sprite = null
mySprite = sprites.create(, SpriteKind.Player)
scene.setBackgroundImage()
mySprite.setPosition(10, 57)
animation.runImageAnimation(
mySprite,
[],
100,
true
)
controller.moveSprite(mySprite, 75, 75)
info.setLife(3)
mySprite.setStayInScreen(true)
boss_hleth = 1
dave = 0
forever(function () {
    if (dave == 0) {
        pause(3000)
        mySprite3 = sprites.create(, SpriteKind.Enemy)
        animation.runImageAnimation(
        mySprite3,
        [],
        100,
        true
        )
    } else if (dave == 1) {
        pause(2000)
        mySprite3 = sprites.create(, SpriteKind.Enemy)
        animation.runImageAnimation(
        mySprite3,
        [],
        100,
        true
        )
        mySprite5 = sprites.create(, SpriteKind.Enemy)
        animation.runImageAnimation(
        mySprite5,
        [],
        100,
        true
        )
        mySprite5.setVelocity(50, 0)
        mySprite5.setPosition(4, randint(10, 111))
    }
    mySprite3.setVelocity(-50, 0)
    mySprite3.setPosition(153, randint(10, 111))
})
forever(function () {
    if (boss_hleth == 0) {
        info.changeScoreBy(100)
        pause(100)
        game.gameOver(true)
    }
})
forever(function () {
    if (dave == 0) {
        pause(3000)
        mySprite2 = sprites.create(, SpriteKind.Food)
        projectile2 = 0
        mySprite2.setVelocity(-50, 0)
        mySprite2.setPosition(151, randint(10, 111))
        animation.runImageAnimation(
        mySprite2,
        [],
        100,
        true
        )
    }
})
