// Copyright 

#include "GroupProject.h"
#include "AIShootingCharacter.h"
#include "PlayerCharacter.h"
#include "EnemyController.h"
#include "BehaviorTree/BehaviorTree.h"
#include "Perception/PawnSensingComponent.h"
#include "WeaponBase.h"

AAIShootingCharacter::AAIShootingCharacter()
{
	PawnSensingComp = CreateDefaultSubobject<UPawnSensingComponent>(TEXT("PawnSensingComp"));
	PawnSensingComp->SetPeripheralVisionAngle(60.0f);
	PawnSensingComp->SightRadius = 2000;
	PawnSensingComp->HearingThreshold = 600;
	PawnSensingComp->LOSHearingThreshold = 1200;

	//Setting the starting AI state to passive 
	States = EAIState::Passive;
}
void AAIShootingCharacter::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	/* Check if the last time we sensed a player is beyond the time out value to prevent from endlessly following a player. */
	if (bSensedTarget && (GetWorld()->TimeSeconds - LastSeenTime) > SenseTimeOut)
	{
		AEnemyController* AIController = Cast<AEnemyController>(GetController());
		if (AIController)
		{
			bSensedTarget = false;
			/* Reset */
			AIController->SetSeenEnemy(nullptr);
			UE_LOG(LogTemp, Warning, TEXT("Target Reset"))
		}
	}

	StartWeaponFire();
}

void AAIShootingCharacter::BeginPlay()
{
	Super::BeginPlay();

	if (PawnSensingComp)
	{
		//This is an event where if the player is seen it will call onseenplayer method
		PawnSensingComp->OnSeePawn.AddDynamic(this, &AAIShootingCharacter::OnSeePlayer);
		//If the AI hears a noise it will call the method on hear noise
		PawnSensingComp->OnHearNoise.AddDynamic(this, &AAIShootingCharacter::OnHearNoise);
	}
	
	//Spawn the weapon on begin play
	if (StartingWeaponBlueprint)
	{
		//Spawning the weapon
		AWeaponBase* StartingWeapon = GetWorld()->SpawnActor<AWeaponBase>(
			StartingWeaponBlueprint,
			GetMesh()->GetSocketLocation(WeaponSocketName),
			GetMesh()->GetSocketRotation(WeaponSocketName)
			);

		//Adding the Weapon to the AI's inventory
		AddToInventory(StartingWeapon);
	}
}

void AAIShootingCharacter::AddToInventory(AWeaponBase * NewWeapon)
{
	//TODO - DestroyGun when the they are killed
	NewWeapon->SetCanInteract(false);//We dont want the player or other enemies to pick it up again
	NewWeapon->SetActorEnableCollision(false);
	NewWeapon->ChangeOwner(this);//Select to new gun
	//Attach to the AI 
	NewWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, WeaponSocketName);//Attching the new weapon to the weapon socket - New to update
	//And store it in the array
	Inventory.AddUnique(NewWeapon);
	CurrentWeaponon = NewWeapon;//This than stores the weapon as the current weapon.
	/*The way its down now can be improved dramtically but the AI only needs one weapon so its fine for the now*/
}

void AAIShootingCharacter::AddWeapon(AWeaponBase* Weapon)
{

}

/*If the AI see the enemy it will set the pawn instigator as a target and move to it */
void AAIShootingCharacter::OnSeePlayer(APawn * PawnInstigator)
{

	/* Keep track of the time the player was last sensed in order to clear the target */
	LastSeenTime = GetWorld()->GetTimeSeconds();
	bSensedTarget = true;

	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	APlayerCharacter* SensedPawn = Cast<APlayerCharacter>(PawnInstigator);
	if (AIController)
	{
		UE_LOG(LogTemp, Warning, TEXT("I See you"))
		AIController->SetSeenEnemy(SensedPawn);
	}
}

/*If we the ai hears a noise this function is called*/
/*When this is called it gets the noise location of the pawninstigator and moves to that location*/
void AAIShootingCharacter::OnHearNoise(APawn * PawnInstigator, const FVector & Location, float Volume)
{

	UE_LOG(LogTemp, Warning, TEXT("I hear you"))
	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	
	if (AIController)
	{
		AIController->SetNoiseLocation(Location);
	}
}

void AAIShootingCharacter::SetState(EAIState NewStates)
{
	States = NewStates;
}



float AAIShootingCharacter::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
{
	int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero


	CurrentHealth -= DamageToApply;
	if (CurrentHealth <= 0)//Check to see if AI is dead
	{
		OnDeath();

	}

	return DamageToApply;
}

/*Weapon*/

void AAIShootingCharacter::StartWeaponFire()
{
	if (CurrentWeaponon)//Check if current weapon is set in the AI
	{
		CurrentWeaponon->StartFire();
	}
}

void AAIShootingCharacter::StopWeaponFire()
{
	if (CurrentWeaponon)//Check if current weapon is set in the AI
	{
		CurrentWeaponon->StopFire();
	}
}