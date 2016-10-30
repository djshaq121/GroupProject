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

	CameraZoomLength = SpringArm->TargetArmLength;
}

// Called when the game starts or when spawned
void APlayerCharacter::BeginPlay()
{
	Super::BeginPlay();
	CurrentHealth = MaximumHealth;
	CurrentArmor = MaximumArmor;
}

// Called every frame
void APlayerCharacter::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );
	//This is what makes the zoomIN/OUT smooth 
	this->SpringArm->TargetArmLength = FMath::FInterpTo(this->SpringArm->TargetArmLength, CameraZoomLength, DeltaTime, 9.0f);//Change the interpSpeed to make smooth longer or more faster
}



//If the player takes damage this method is called
float APlayerCharacter::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
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
				//UE_LOG(LogTemp, Warning, TEXT("Player is dead"))
					//OnDeath() - Destroies the player and restarts the game
					OnDeath.Broadcast();
				isDead = true;//Sets it to true, so in blueprint it plays the death animation 
				StopAnimMontage();
			}
			else
			{
				isDead = false;
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

int APlayerCharacter::GetCurrentHealth() const
{
	return CurrentHealth;
}

int APlayerCharacter::GetCurrentArmor() const
{
	return CurrentArmor;
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
	if (SpringArm->TargetArmLength > 150.f)//Checks to see if the spring arm is bigger than the minimum value we set
	{
		CameraZoomLength -= 250.f; // decrease the length of the springarm 
		if (CameraZoomLength < 150.f)
		{
			CameraZoomLength = 150.f;//making sure if we decrease it past 150, it stays at 150 
		}
	}
}

void APlayerCharacter::CameraZoomOut()
{
	if (SpringArm->TargetArmLength < 400.f)// Cheacks to see if we are bigger than our maximum camera length
	{
		CameraZoomLength += 250.f; //Adds back the length we decrease from the zoom out
		if (CameraZoomLength > 400.f) //Checks to see if we are above 400
		{
			CameraZoomLength = 400.f;//If so set arm length back to 400
		}
	}
}

//This gets the controller of the pawn
AHumanPlayerController* APlayerCharacter::GetHumanController()
{
	return Cast<AHumanPlayerController>(GetController());
}

