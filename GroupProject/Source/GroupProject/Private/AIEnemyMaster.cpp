// Copyright 

#include "GroupProject.h"
#include "AIEnemyMaster.h"


// Sets default values
AAIEnemyMaster::AAIEnemyMaster(const FObjectInitializer& ObjectInitializer)
	: Super(ObjectInitializer)
{
 	
}

// Called when the game starts or when spawned
void AAIEnemyMaster::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void AAIEnemyMaster::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );

}

float AAIEnemyMaster::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
{
	int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero
	int32 DamageToApplyArmor = FMath::Clamp(DamagePoint, 0, CurrentArmor);//This clamps the damage point between 0 and current armor. So armor cant go below zero
																		  //UE_LOG(LogTemp, Warning, TEXT("DamageAmount: %f, DamageToApply: %i"), DamageAmount, DamageToApply)
																		  //CurrentArmor = FMath::Clamp(CurrentArmor, 0, 100);

																		  //isTakingDamage = true;



	if (CurrentArmor <= 0)
	{
		CurrentHealth -= DamageToApply;
		if (CurrentHealth <= 0)
		{
			UE_LOG(LogTemp, Warning, TEXT("AI is dead"))
			//GetWorldTimerManager().SetTimer(UnusedHandle, this, &AAIPatrol::TimerElapsed, TimerDelay, false);
		}
		else
		{
			//
		}
	}
	else
	{
		CurrentArmor -= DamageToApplyArmor;
		if (CurrentArmor <= 0)
		{
			//UE_LOG(LogTemp, Warning, TEXT("Armor Depleted"))
		}
	}


	return DamageToApply;
}