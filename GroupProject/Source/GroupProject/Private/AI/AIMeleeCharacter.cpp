// Copyright 

#include "GroupProject.h"
#include "AIMeleeCharacter.h"
#include "PlayerCharacter.h"
#include "EnemyController.h"
#include "BehaviorTree/BehaviorTree.h"

AAIMeleeCharacter::AAIMeleeCharacter() 
{
	MeleeCollisionComp = CreateDefaultSubobject<UCapsuleComponent>(TEXT("MeleeCollision"));
	MeleeCollisionComp->SetRelativeLocation(FVector(45, 0, 25));
	MeleeCollisionComp->SetCapsuleHalfHeight(60);
	MeleeCollisionComp->SetCapsuleRadius(35, false);
	MeleeCollisionComp->SetCollisionResponseToAllChannels(ECR_Ignore);
	MeleeCollisionComp->SetCollisionResponseToChannel(ECC_Pawn, ECR_Overlap);
	MeleeCollisionComp->SetupAttachment(GetCapsuleComponent());

	MeleeDamage = 24.0f;
	MeleeStrikeCooldown = 1.0f;
}

void AAIMeleeCharacter::Tick(float DeltaSeconds)
{
	Super::Tick(DeltaSeconds);

	/* Check if the last time we sensed a player is beyond the time out value to prevent bot from endlessly following a player. */
	
	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	
	if (AIController)
	{
		/* Reset */
			AIController->SetTargetEnemy(nullptr);

	}
	
}
// Called when the game starts or when spawned
void AAIMeleeCharacter::BeginPlay()
{
	Super::BeginPlay();

	CurrentHealth = MaximumHealth;
	if (MeleeCollisionComp)
	{
		MeleeCollisionComp->OnComponentBeginOverlap.AddDynamic(this, &AAIMeleeCharacter::OnMeleeCompBeginOverlap);
	}

}

void AAIMeleeCharacter::PerformMeleeStrike(AActor* HitActor)
{
	if (LastMeleeAttackTime > GetWorld()->GetTimeSeconds() - MeleeStrikeCooldown)
	{
		/* Set timer to start attacking as soon as the cooldown elapses. */
		if (!TimerHandle_MeleeAttack.IsValid())
		{
			// TODO: Set Timer
		}

		/* Attacked before cooldown expired */
		return;
	}

	if (HitActor)
	{
		APlayerCharacter* OtherPawn = Cast<APlayerCharacter>(HitActor);
		if (OtherPawn)
		{
			/* Set to prevent a zombie to attack multiple times in a very short time */
			LastMeleeAttackTime = GetWorld()->GetTimeSeconds();

			FPointDamageEvent DmgEvent;
			DmgEvent.DamageTypeClass = PunchDamageType;
			DmgEvent.Damage = MeleeDamage;

			HitActor->TakeDamage(DmgEvent.Damage, DmgEvent, GetController(), this);

			SimulateMeleeStrike();
		}
	}
}


void AAIMeleeCharacter::OnMeleeCompBeginOverlap(class UPrimitiveComponent* OverlappedComponent, class AActor* OtherActor, class UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFromSweep, const FHitResult & SweepResult)
{
	/* Stop any running attack timers */
	TimerHandle_MeleeAttack.Invalidate();

	PerformMeleeStrike(OtherActor);

	/* Set re-trigger timer to re-check overlapping pawns at melee attack rate interval */
	GetWorldTimerManager().SetTimer(TimerHandle_MeleeAttack, this, &AAIMeleeCharacter::OnRetriggerMeleeStrike, MeleeStrikeCooldown, true);
}

void AAIMeleeCharacter::SimulateMeleeStrike_Implementation()
{
	PlayAnimMontage(MeleeAnimMontage);
	PlayCharacterSound(SoundAttackMelee);
}

UAudioComponent* AAIMeleeCharacter::PlayCharacterSound(USoundCue* CueToPlay)
{
	if (CueToPlay)
	{
		return UGameplayStatics::SpawnSoundAttached(CueToPlay, RootComponent, NAME_None, FVector::ZeroVector, EAttachLocation::SnapToTarget, true);
	}

	return nullptr;
}

void AAIMeleeCharacter::OnRetriggerMeleeStrike()
{
	/* Apply damage to a single random pawn in range. */
	TArray<AActor*> Overlaps;
	MeleeCollisionComp->GetOverlappingActors(Overlaps, APlayerCharacter::StaticClass());
	for (int32 i = 0; i < Overlaps.Num(); i++)
	{
		APlayerCharacter* OverlappingPawn = Cast<APlayerCharacter>(Overlaps[i]);
		if (OverlappingPawn)
		{
			PerformMeleeStrike(OverlappingPawn);
			//break; /* Uncomment to only attack one pawn maximum */
		}
	}

	/* No pawns in range, cancel the retrigger timer */
	if (Overlaps.Num() == 0)
	{
		TimerHandle_MeleeAttack.Invalidate();
	}
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
	MeleeCollisionComp->SetCollisionEnabled(ECollisionEnabled::NoCollision);
	MeleeCollisionComp->SetCollisionResponseToAllChannels(ECR_Ignore);
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
