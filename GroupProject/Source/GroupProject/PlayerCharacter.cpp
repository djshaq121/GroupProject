// Copyright 

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "HumanPlayerController.h"


// Sets default values
APlayerCharacter::APlayerCharacter()
{
 	// Set this character to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	//PrimaryActorTick.bCanEverTick = true;

	// set our turn rates for input
	BaseTurnRate = 45.f;
	BaseLookUpRate = 45.f;


	SpringArm = CreateDefaultSubobject<USpringArmComponent>(TEXT("SpringArm"));
	SpringArm->SetupAttachment(RootComponent);
	SpringArm->TargetArmLength = 400.f;//Setting the length of the cameraboom
	SpringArm->SocketOffset = FVector(0, 40, 120);//Setting the position of the camera 
	SpringArm->bUsePawnControlRotation = true;

	Camera = CreateDefaultSubobject<UCameraComponent>(TEXT("Camera"));
	Camera->SetupAttachment(SpringArm, USpringArmComponent::SocketName);
	Camera->bUsePawnControlRotation = false;

	CameraZoom = SpringArm->TargetArmLength;
}

// Called when the game starts or when spawned
void APlayerCharacter::BeginPlay()
{
	Super::BeginPlay();
	
}

// Called every frame
void APlayerCharacter::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );

}

// Called to bind functionality to input
void APlayerCharacter::SetupPlayerInputComponent(class UInputComponent* InputComponent)
{
	Super::SetupPlayerInputComponent(InputComponent);

	InputComponent->BindAxis("Turn", this, &APlayerCharacter::TurnAtRate);
	InputComponent->BindAxis("LookUp", this, &APlayerCharacter::LookUpRate);

	InputComponent->BindAxis("MoveForward", this, &APlayerCharacter::MoveForward);
	InputComponent->BindAxis("MoveRight", this, &APlayerCharacter::MoveRight);

	InputComponent->BindAction("Zoom", IE_Pressed, this, &APlayerCharacter::CameraZoomIn);
	InputComponent->BindAction("Zoom", IE_Released, this, &APlayerCharacter::CameraZoomOut);


	InputComponent->BindAction("Fire", IE_Pressed, this, &APlayerCharacter::OnFire);

	//InputComponent->BindAction("Jump", IE_Pressed, this, &ACharacter::Jump);
	//InputComponent->BindAction("Jump", IE_Released, this, &ACharacter::StopJumping);

	

}


void APlayerCharacter::OnFire()
{


	//This calls the method 'AimTowardsCrosshair' everytime is pressed
	//ATPSHumanController* PlayerController = Cast<ATPSHumanController>(GetController());


	if (GetHumanController())//Checks if the player has a controller
	{
		//Calls the method from the controller
		GetHumanController()->AimTowardsCrosshair();
	}
	else
	{
		UE_LOG(LogTemp, Warning, TEXT("Fire Not Working"));
	}
	
}

void APlayerCharacter::MoveForward(float Value)
{
	if ((Controller != NULL) && (Value != 0.0f))
	{
		// find out which way is forward
		const FRotator Rotation = Controller->GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// get forward vector
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::X);
		AddMovementInput(Direction, Value);
	}
}

void APlayerCharacter::MoveRight(float Value)
{
	if ((Controller != NULL) && (Value != 0.0f))
	{
		// find out which way is right
		const FRotator Rotation = Controller->GetControlRotation();
		const FRotator YawRotation(0, Rotation.Yaw, 0);

		// get right vector 
		const FVector Direction = FRotationMatrix(YawRotation).GetUnitAxis(EAxis::Y);
		// add movement in that direction
		AddMovementInput(Direction, Value);
	}
}

void APlayerCharacter::TurnAtRate(float Rate)
{
	AddControllerYawInput(Rate * BaseTurnRate * GetWorld()->GetDeltaSeconds());
}

void APlayerCharacter::LookUpRate(float Rate)
{
	AddControllerPitchInput(Rate * BaseLookUpRate * GetWorld()->GetDeltaSeconds());
}

void APlayerCharacter::CameraZoomIn()
{
	
	//CameraZoom set to tragetarmlength
	//400-300 = 100
	CameraZoom = CameraZoom - CameraZoomLength;//TargetArmLenth subtracted by the length we want to Zoom in by 

	//We check if CameraZoom is bigger than 100, if true set the armlength 
	if (CameraZoom <= 150.f)
	{
		SpringArm->TargetArmLength = 150;
		CameraZoom = 150.F;
		UE_LOG(LogTemp,Warning, TEXT("Working"))
	}
	else
	{
		//This condition is excuteded when the CameraZoom i smore than the desired zoom
		SpringArm->TargetArmLength = CameraZoom;
		UE_LOG(LogTemp, Warning, TEXT("Shouldnt be called"))
	}
}

void APlayerCharacter::CameraZoomOut()
{
	//100+300 = 400
	CameraZoom = CameraZoom + CameraZoomLength;

	if (CameraZoom >= 400.f)
	{
		SpringArm->TargetArmLength = 400.f;
		CameraZoom = 400.f;
		UE_LOG(LogTemp, Warning, TEXT("Working1"))
	}
	else
	{
		SpringArm->TargetArmLength = CameraZoom;
		UE_LOG(LogTemp, Warning, TEXT("Shouldnt be called1"))
	}
}

//This gets the controller of the pawn
AHumanPlayerController* APlayerCharacter::GetHumanController()
{
	return Cast<AHumanPlayerController>(GetController());
}

