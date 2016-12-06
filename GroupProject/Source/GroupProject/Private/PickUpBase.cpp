// Copyright 

#include "GroupProject.h"
#include "PickUpBase.h"


// Sets default values
APickUpBase::APickUpBase()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	PickUpRoot = CreateDefaultSubobject<USceneComponent>(TEXT("PickupRoot"));
	RootComponent = PickUpRoot;

	PickupMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("PickUpMesh"));
	PickupMesh->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);

	PickupBox = CreateDefaultSubobject<UBoxComponent>(TEXT("CollisionBox"));
	PickupBox->bGenerateOverlapEvents = true;//Turning on overlap events
	PickupBox->OnComponentBeginOverlap.AddDynamic(this, &APickUpBase::OnPlayerEnterPickupBox);
	PickupBox->AttachToComponent(RootComponent, FAttachmentTransformRules::KeepRelativeTransform);
}

// Called when the game starts or when spawned
void APickUpBase::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void APickUpBase::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );

}

void APickUpBase::OnPlayerEnterPickupBox(UPrimitiveComponent* OverlappedComp, AActor* OtherActor, UPrimitiveComponent* OtherComp, int32 OtherBodyIndex, bool bFomSweep, const FHitResult& SweepResult)
{
	UE_LOG(LogTemp, Warning, TEXT("Overlapping"))
		//Maybe add to inventory or Add health 
}
