// Copyright 

#include "GroupProject.h"
#include "AIEnemyMaster.h"


// Sets default values


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
	//int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	//int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero
	//
	UE_LOG(LogTemp,Warning,TEXT("Not to be called"))
	return DamageAmount;
}

int AAIEnemyMaster::GetCurrentHealth() const
{
	return CurrentHealth;
}