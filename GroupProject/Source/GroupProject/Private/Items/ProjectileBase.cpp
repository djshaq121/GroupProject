// Copyright LostGods

#include "GroupProject.h"
#include "ProjectileBase.h"
#include "PlayerCharacter.h"


// Sets default values
AProjectileBase::AProjectileBase()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;

	CollisonSphere = CreateDefaultSubobject<USphereComponent>(TEXT("CollisonSphere"));
	SetRootComponent(CollisonSphere);

	BulletMesh = CreateDefaultSubobject<USkeletalMeshComponent>(TEXT("BulletMesh"));
	BulletMesh->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);

	ProjectileMovement = CreateDefaultSubobject<UProjectileMovementComponent>(FName("Projectile Movement"));

}

// Called when the game starts or when spawned
void AProjectileBase::BeginPlay()
{
	Super::BeginPlay();
	CollisonSphere->OnComponentHit.AddDynamic(this, &AProjectileBase::OnHit);
}

// Called every frame
void AProjectileBase::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );

}

void AProjectileBase::DealDamage(const FHitResult& Hit)
{


	if (Hit.GetActor())
	{
		float DealtDamage = BaseDamage;//Later maybe damage multipler 
		FVector ShotDirection = GetActorLocation() - Hit.ImpactPoint;//Gets the location of the gun subtract from the hit point location to find the direction

																	 //This fully describes the damage recieved 
		FPointDamageEvent DamageEvent;
		DamageEvent.Damage = DealtDamage;
		DamageEvent.HitInfo = Hit;
		//DamageEvent.ShotDirection = ShotDirection;
		DamageEvent.ShotDirection.Normalize();

		//Calls the method on the actor that takes damage
		/*Crashes if the player is still shooting, hits an actor and dies */
		
		Hit.GetActor()->TakeDamage(DealtDamage, DamageEvent, GetInstigatorController(),this);//Crashes at this line

																									
	}


}

void AProjectileBase::OnHit(UPrimitiveComponent* HitComponent, AActor* OtherActor, UPrimitiveComponent* OtherComponent, FVector NormalImpulse, const FHitResult& Hit)
{
	/*LaunchBlast->Deactivate();
	ImpactBlast->Activate();
	ExplosionForce->FireImpulse();

	SetRootComponent(ImpactBlast);
	CollisionMesh->DestroyComponent();*/
	
	if (Hit.GetActor())
	{
		
		APlayerCharacter* PlayerCharacter = Cast<APlayerCharacter>(OtherActor);
		if (PlayerCharacter)
		{
			UE_LOG(LogTemp, Warning, TEXT("Hitting"))
			DealDamage(Hit);
			//GetWorld()->GetFirstPlayerController()->GetPawn()
		}
	}

	Destroy();

	/*FTimerHandle Timer;
	GetWorld()->GetTimerManager().SetTimer(Timer, this, &AProjectileBase::OnTimerExpire, DestroyDelay, false);*/
}

void AProjectileBase::OnTimerExpire()
{
	Destroy();
}
