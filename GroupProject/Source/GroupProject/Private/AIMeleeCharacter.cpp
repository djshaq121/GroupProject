// Copyright 

#include "GroupProject.h"
#include "AIMeleeCharacter.h"
#include "BehaviorTree/BehaviorTree.h"

AAIMeleeCharacter::AAIMeleeCharacter() 
{

}


// Called when the game starts or when spawned
void AAIMeleeCharacter::BeginPlay()
{
	Super::BeginPlay();

	CurrentHealth = MaximumHealth;
	

}

int AAIMeleeCharacter::GetCurrentHealth() const
{
	return CurrentHealth;
}

void AAIMeleeCharacter::SetRagdollPhysics()
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

void AAIMeleeCharacter::OnDeath()
{
	UE_LOG(LogTemp, Warning, TEXT("AI is dead"))
	SetRagdollPhysics();
	DetachFromControllerPendingDestroy();

	/* Disable all collision on capsule */
	UCapsuleComponent* CapsuleComp = GetCapsuleComponent();
	CapsuleComp->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	CapsuleComp->SetCollisionResponseToAllChannels(ECR_Ignore);
}

float AAIMeleeCharacter::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
{
	int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero

	CurrentHealth -= DamageToApply;
	if (CurrentHealth <= 0)//Check to see if AI is dead
	{
		OnDeath();

	}
	UE_LOG(LogTemp, Warning, TEXT("Taking damage"))
	return DamageToApply;
}
