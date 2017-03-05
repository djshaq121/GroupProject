// Copyright 

#include "GroupProject.h"
#include "AIMeleeCharacter.h"
#include "PlayerCharacter.h"
#include "EnemyController.h"
#include "BehaviorTree/BehaviorTree.h"
#include "Perception/PawnSensingComponent.h"
#include "WaveGameMode.h"

AAIMeleeCharacter::AAIMeleeCharacter() 
{

	PawnSensingComp = CreateDefaultSubobject<UPawnSensingComponent>(TEXT("PawnSensingComp"));
	PawnSensingComp->SetPeripheralVisionAngle(60.0f);
	PawnSensingComp->SightRadius = 2000;
	PawnSensingComp->HearingThreshold = 600;
	PawnSensingComp->LOSHearingThreshold = 1200;
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
	/* Check if the last time we sensed a player is beyond the time out value to prevent from endlessly following a player. */
	if (bSensedTarget && (GetWorld()->TimeSeconds - LastSeenTime) > SenseTimeOut)
	{
		AEnemyController* AIController = Cast<AEnemyController>(GetController());
		if (AIController)
		{
			bSensedTarget = false;
			/* Reset */
			AIController->SetTargetEnemy(nullptr);
		}
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

	if (PawnSensingComp)
	{
		//if play is caught call the OnPlayerCaught function
		PawnSensingComp->OnSeePawn.AddDynamic(this, &AAIMeleeCharacter::OnSeePlayer);
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


void AAIMeleeCharacter::OnSeePlayer(APawn* Pawn)
{
	
	/* Keep track of the time the player was last sensed in order to clear the target */
	LastSeenTime = GetWorld()->GetTimeSeconds();
	bSensedTarget = true;
	
	AEnemyController* AIController = Cast<AEnemyController>(GetController());
	APlayerCharacter* SensedPawn = Cast<APlayerCharacter>(Pawn);
	if (AIController)
	{
		if (SensedPawn)
		{
			AIController->SetTargetEnemy(SensedPawn);
		}
		
		
	}
}

void AAIMeleeCharacter::OnDeath()
{
	
	SetRagdollPhysics();
	//DetachFromControllerPendingDestroy();

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
		
		AWaveGameMode* WaveGM = GetWorld()->GetAuthGameMode<AWaveGameMode>();
		if (WaveGM)
		{
			//APlayerCharacter* Killer = Cast<APlayerCharacter>(Caller);
			WaveGM->Killed(EventInstigator, GetController());
			OnDeath();
		}
		
	}
	
	return DamageToApply;
}
