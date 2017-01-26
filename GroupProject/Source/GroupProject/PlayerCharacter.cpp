// Copyright 

#include "GroupProject.h"
#include "PlayerCharacter.h"
#include "HumanPlayerController.h"
#include "AssaultRifleBase.h"
#include "LaserRifleBase.h"
#include "WeaponBase.h"


/*Created a custom preset in the Player_BP so that ECC_weapons ignores the Player_BP*/



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
	SpringArm->TargetArmLength = 300.f;//Setting the length of the cameraboom
	SpringArm->SocketOffset = FVector(0, 50, 50);//Setting the position of the camera 
	SpringArm->bUsePawnControlRotation = true;

	Camera = CreateDefaultSubobject<UCameraComponent>(TEXT("Camera"));
	Camera->SetupAttachment(SpringArm, USpringArmComponent::SocketName);
	Camera->bUsePawnControlRotation = false;

	
	CamCrouchHeight = SpringArm->SocketOffset.Z;
	
	CameraZoomLength = SpringArm->TargetArmLength;

	//Initialise the can crouch property
	GetCharacterMovement()->GetNavAgentPropertiesRef().bCanCrouch = true;

	/* Ignore this channel or it will absorb the trace impacts instead of the skeletal mesh */
	GetCapsuleComponent()->SetCollisionResponseToChannel(ECC_Weapon, ECR_Ignore);

	
}

// Called when the game starts or when spawned
void APlayerCharacter::BeginPlay()
{
	Super::BeginPlay();
	CurrentHealth = MaximumHealth;
	CurrentArmor = MaximumArmor;

	GetCharacterMovement()->MaxWalkSpeed = WalkSpeed;
	
}

// Called every frame
void APlayerCharacter::Tick( float DeltaTime )
{
	Super::Tick( DeltaTime );
	//This is what makes the zoomIN/OUT smooth 
	this->SpringArm->TargetArmLength = FMath::FInterpTo(this->SpringArm->TargetArmLength, CameraZoomLength, DeltaTime, 15.0f);//Change the interpSpeed to make smooth longer or more faster
	//This makes a smooth transition when the player is crouched
	SpringArm->SocketOffset.Z = FMath::FInterpTo(this->SpringArm->SocketOffset.Z, CamCrouchHeight, DeltaTime, 15.0f);
	
	if (bIsSprinting && CheckIfCanSprint())
	{
		SetSprint(true);
	}
	else
	{
		SetSprint(false);
	}
	
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

	InputComponent->BindAction("Crouch", IE_Pressed, this, &APlayerCharacter::ToggleCrouch);

	InputComponent->BindAction("Sprint", IE_Pressed, this, &APlayerCharacter::StartSprint);
	InputComponent->BindAction("Sprint", IE_Released, this, &APlayerCharacter::EndSprint);

	InputComponent->BindAction("Fire", IE_Pressed, this, &APlayerCharacter::StartFire);
	InputComponent->BindAction("Fire", IE_Released, this, &APlayerCharacter::StopFire);
	InputComponent->BindAction("Reload", IE_Pressed, this, &APlayerCharacter::Reload);
	InputComponent->BindAction("SwitchAssault", IE_Released, this, &APlayerCharacter::SwitchToAssaultRifle);
	InputComponent->BindAction("SwitchLaser", IE_Released, this, &APlayerCharacter::SwitchToLaserLaser);

	InputComponent->BindAction("Jump", IE_Pressed, this, &APlayerCharacter::OnJump);
	InputComponent->BindAction("Jump", IE_Released, this, &APlayerCharacter::EndJump);
	

	

}

void APlayerCharacter::OnJump()
{
	SetIsJumping(true);
	
}

void APlayerCharacter::EndJump()
{
	SetIsJumping(false);
}

void APlayerCharacter::SetIsJumping(bool newJumpState)
{
	JumpHeight = GetCharacterMovement()->JumpZVelocity;
	
	
	if (newJumpState!= bIsJumping)
	{
		bIsJumping = newJumpState;

		if (GetCharacterMovement()->MaxWalkSpeed == WalkSpeed)
		{
			
			JumpHeight = 300.f;
			Jump();
			
		}
		else if (GetCharacterMovement()->MaxWalkSpeed == SprintSpeed)
		{
			
			JumpHeight = 400.f;
			Jump();
			
		}
	}
	else
	{
		bIsJumping = false;
	}
	//bIsJumping = false;
}

bool APlayerCharacter::GetIsJumping() const
{
	return bIsJumping;
}

void APlayerCharacter::ToggleCrouch()
{
	
	if (!bIsCrouching)
	{
		Crouching();
	
	}
	else
	{
		UnCrouching();
		
	}
}

void APlayerCharacter::Crouching()
{
	bIsCrouching = true;
	CamCrouchHeight = 30.f;

}

void APlayerCharacter::UnCrouching()
{
	CamCrouchHeight = 50.f;
	bIsCrouching = false;

}

bool APlayerCharacter::GetIsCrouching() const
{
	return bIsCrouching;
}


void APlayerCharacter::StartSprint()
{
	SetSprint(true);
}

void APlayerCharacter::EndSprint()
{
	SetSprint(false);
}

void APlayerCharacter::SetSprint(bool NewSprintState)
{
	bIsSprinting = NewSprintState;

	if (bIsSprinting)
	{
		GetCharacterMovement()->MaxWalkSpeed = SprintSpeed;
		if (bIsCrouching)//If we are crouching, uncrouch before we run running 
		{
			UnCrouching();
		}
	}
	else
	{
		GetCharacterMovement()->MaxWalkSpeed = WalkSpeed;
	}

}

bool APlayerCharacter::GetIsSprinting() const
{
	return bIsSprinting;
}


void APlayerCharacter::SetPlayersSpeed(bool NewSprintState)
{
	bIsSprinting = NewSprintState;

}

bool APlayerCharacter::CheckIfCanSprint()
{
	return bIsSprinting && !bIsFiring &&
		!GetVelocity().IsZero() &&
		!GetIsAiming() && 
		(FVector::DotProduct(GetVelocity().GetSafeNormal2D(), GetActorRotation().Vector()) > 0.8);//Checks to see if the player is moving forward, and if they are set to true else false - Taken from tomlooman
}

bool APlayerCharacter::GetIsAiming() const
{
	return bIsAiming;
}

void APlayerCharacter::StartFire()
{

		if (Inventory.CurrentWeapon)
		{
			bIsFiring = true;
			Inventory.CurrentWeapon->StartFire();
		}

}



void APlayerCharacter::StopFire()
{
	if (Inventory.CurrentWeapon)
	{
		bIsFiring = false;
		Inventory.CurrentWeapon->StopFire();
	}
}

void APlayerCharacter::Reload()
{
	if (Inventory.CurrentWeapon)
	{
		Inventory.CurrentWeapon->Reload();
	}
}

void APlayerCharacter::SwitchToAssaultRifle()
{


	if (Inventory.AssaultRifle)
	{

		EquipWeapon(Inventory.AssaultRifle);
	}
}

void APlayerCharacter::SwitchToLaserLaser()
{
	if (Inventory.LaserRifle)
	{

		EquipWeapon(Inventory.LaserRifle);
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
 

void APlayerCharacter::Heal(int Amount)
{
	// Currently polayer can still pickup when his health is 100 and item is destroyed but no health is gained
	if (CurrentHealth < 100)
	{
		CurrentHealth = CurrentHealth + Amount;
		UE_LOG(LogTemp, Warning, TEXT("Health: %f"), CurrentHealth)
	}
}

bool APlayerCharacter::GetIsDead()
{
	return bIsDead;
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

//If the player takes damage this method is called
float APlayerCharacter::TakeDamage(float DamageAmount, FDamageEvent const & DamageEvent, AController * EventInstigator, AActor * DamageCauser)
{
	int32 DamagePoint = FPlatformMath::RoundToInt(DamageAmount);//Convert floating point damage to int damage and then round the damage
	int32 DamageToApply = FMath::Clamp(DamagePoint, 0, CurrentHealth);//This clamps the damage point between 0 and current health. So health cant go below zero
	int32 DamageToApplyArmor = FMath::Clamp(DamagePoint, 0, CurrentArmor);//This clamps the damage point between 0 and current armor. So armor cant go below zero


	if (CurrentArmor <= 0)
	{
		CurrentHealth -= DamageToApply;
		if (CurrentHealth <= 0)
		{
			//UE_LOG(LogTemp, Warning, TEXT("Player is dead"))
			//OnDeath() - Destroies the player and restarts the game
			OnDeath.Broadcast();
			bIsDead = true;//Sets it to true, so in blueprint it plays the death animation 
			StopAnimMontage();
		}
		else
		{
			bIsDead = false;
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

void APlayerCharacter::CameraZoomIn()
{
	bIsAiming = true;
		
		if (SpringArm->TargetArmLength > 150.f)//Checks to see if the spring arm is bigger than the minimum value we set
		{
			
			CameraZoomLength -= 150.f; // decrease the length of the springarm 
			
			if (CameraZoomLength < 150.f)
			{
				CameraZoomLength = 150.f;//making sure if we decrease it past 150, it stays at 150 
			}
		}

}

void APlayerCharacter::CameraZoomOut()
{
	bIsAiming = false;
	if (SpringArm->TargetArmLength < 300.f)// Cheacks to see if we are bigger than our maximum camera length
	{
		CameraZoomLength += 150.f; //Adds back the length we decrease from the zoom out
		bIsAiming = false;
		if (CameraZoomLength > 300.f) //Checks to see if we are above 400
		{
			CameraZoomLength = 300.f;//If so set arm length back to 400
		}
	}
}

void APlayerCharacter::AddToInventory(class AWeaponBase* NewWeapon) {


	NewWeapon->SetCanInteract(false);//We dont want to pick it up again
	NewWeapon->SetActorEnableCollision(false);
	NewWeapon->ChangeOwner(this);//Select to new gun
	
	//Check if we have a weapon in our invenontry 
	//if (Inventory.CurrentWeapon)
	//{
	//	//Inventory.CurrentWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, SecondWeaponSocket);//Attach the previous weapon on the back of the player
	//	Inventory.PreviousWeapon = Inventory.CurrentWeapon;//Storing the current weapon to previous weapon
	//}
	//
	NewWeapon->AttachToComponent(GetMesh(),FAttachmentTransformRules::SnapToTargetIncludingScale, WeaponSocketName);//Attching the new weapon to the weapon socket - New to update
	
	//if weapon is AssaultRifleBase
	if (NewWeapon->IsA(AAssaultRifleBase::StaticClass())) {
		if (Inventory.AssaultRifle) {
			Inventory.AssaultRifle->Destroy();
		}
		Inventory.AssaultRifle = Cast<AAssaultRifleBase>(NewWeapon);

		if (!Inventory.CurrentWeapon || bEquipNewWeapon) {//bEquipnew weapon allows the user to equipt the weapon upon pick up
			EquipWeapon(Inventory.AssaultRifle);
			

		}
	}
	//if weapon is laser rifle
	else if (NewWeapon->IsA(ALaserRifleBase::StaticClass())) {
		if (Inventory.LaserRifle) {
			Inventory.LaserRifle->Destroy();
		}
		Inventory.LaserRifle = Cast<ALaserRifleBase>(NewWeapon);

		if (!Inventory.CurrentWeapon || bEquipNewWeapon) {
			EquipWeapon(Inventory.LaserRifle);
		

		}
	}


}

void APlayerCharacter::EquipWeapon(AWeaponBase * WeaponToEquip)//Check to see if weapon is in the inventory
{
	if (WeaponToEquip == Inventory.CurrentWeapon) {
		return;//Return if we already have the weapon equiped
	}
	
	Inventory.PreviousWeapon = Inventory.CurrentWeapon;//Storing the current weapon to previous weapon

	

	//Check what weapon we are picking up
	if (WeaponToEquip == Inventory.AssaultRifle) {
		Inventory.CurrentWeapon = Inventory.AssaultRifle;//Makes AssaultRifle the currentWeapon
		Inventory.CurrentWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, WeaponSocketName);//Attaches the current weapon to the weapon socket

		if (Inventory.PreviousWeapon)//Checking if previous weapon is null
		{
			//If not null we connect the previous weapon to the back Socket
			Inventory.PreviousWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, SecondWeaponSocket);
			Inventory.PreviousWeapon->StopFire();//Stops the weapon from firing when in the second slot, if the player is holding the fire trigger when equipping a secong weapon
		}
		
	}
	else if (WeaponToEquip == Inventory.LaserRifle) {
		Inventory.CurrentWeapon = Inventory.LaserRifle;//Makes LaserRifle the currentWeapon
		Inventory.CurrentWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, WeaponSocketName);
	
		if (Inventory.PreviousWeapon)
		{
			Inventory.PreviousWeapon->AttachToComponent(GetMesh(), FAttachmentTransformRules::SnapToTargetIncludingScale, SecondWeaponSocket);
			Inventory.PreviousWeapon->StopFire();
		}
	

	
	}//else if...for more types of gun
	

	
}

//This gets the controller of the pawn
AHumanPlayerController* APlayerCharacter::GetHumanController()
{
	return Cast<AHumanPlayerController>(GetController());
}

