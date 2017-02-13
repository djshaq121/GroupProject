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

void AAIEnemyMaster::SetRagdollPhysics()
{
	bool bInRagdoll = false;
	USkeletalMeshComponent* Mesh3P = GetMesh();

	if (IsPendingKill())
	{
		bInRagdoll = false;
	}
	else if (!Mesh3P || !Mesh3P->GetPhysicsAsset())
	{
		bInRagdoll = false;
	}
	else
	{
		Mesh3P->SetAllBodiesSimulatePhysics(true);
		Mesh3P->SetSimulatePhysics(true);
		Mesh3P->WakeAllRigidBodies();
		Mesh3P->bBlendPhysics = true;

		bInRagdoll = true;
	}

	UCharacterMovementComponent* CharacterComp = Cast<UCharacterMovementComponent>(GetMovementComponent());
	if (CharacterComp)
	{
		CharacterComp->StopMovementImmediately();
		CharacterComp->DisableMovement();
		CharacterComp->SetComponentTickEnabled(false);
	}

	if (!bInRagdoll)
	{
		// Immediately hide the pawn
		TurnOff();
		SetActorHiddenInGame(true);
		SetLifeSpan(1.0f);
	}
	else
	{
		SetLifeSpan(10.0f);
	}
}

void AAIEnemyMaster::OnDeath()
{
	SetRagdollPhysics();
	DetachFromControllerPendingDestroy();

	/* Disable all collision on capsule */
	UCapsuleComponent* CapsuleComp = GetCapsuleComponent();
	CapsuleComp->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	CapsuleComp->SetCollisionResponseToAllChannels(ECR_Ignore);
}
