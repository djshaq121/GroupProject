// Copyright 

#pragma once

#include "GameFramework/Character.h"
#include "GroupProject.h"
#include "PlayerCharacter.generated.h"

//Death

DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnDeathRequest);

class ACharacterController;

UCLASS()
class GROUPPROJECT_API APlayerCharacter : public ACharacter
{
	GENERATED_BODY()

		UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class USpringArmComponent* SpringArm;

	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera", meta = (AllowPrivateAccess = "true"))
		class UCameraComponent* Camera;

	/*Health & Armor*/
private:
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumHealth = 100;//Its int because we dont want to compare float to zero

	
		int32 CurrentHealth;


	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		int32 MaximumArmor = 100;//Its int because we dont want to compare float to zero

	
		int32 CurrentArmor;

public:
	UFUNCTION(Client, Reliable)
		void UpdateHUD();

	UFUNCTION(BlueprintImplementableEvent, Category = "HUD")
	void BP_Update();


	UPROPERTY(BlueprintAssignable)
	FOnDeathRequest OnDeathRequest;

	void onDeath();

	void MakePawnNoise(float LoudNess);


	bool bCanInteract = false;

	// Sets default values for this character's properties
	APlayerCharacter();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

	// Called every frame
	virtual void Tick(float DeltaSeconds) override;

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
	virtual float TakeDamage(float DamageAmount, struct FDamageEvent const & DamageEvent, class AController * EventInstigator, AActor * DamageCauser) override;

	// Called to bind functionality to input
	virtual void SetupPlayerInputComponent(class UInputComponent* PlayerInputComponent) override;

	ACharacterController* GetHumanController();

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
		int GetCurrentHealth() const;

	UFUNCTION(BlueprintCallable, Category = "Health & Armor")
		int GetCurrentArmor() const;

	int GetMaxHealth() const;
	
	int GetMaxArmor() const;

	void Heal(int Amount);

	void HealArmor(int Amount);

	UFUNCTION(BlueprintCallable, Category = "Setup")
	bool GetIsDead() const;

	//Interaction
	AActor* GetFocusedActor();

	void HandleFocus();

	void Interact();

	/*Movement*/

public:

	
	void SwapToNewWeaponMesh(AWeaponBase * WeaponToEquip);

	UFUNCTION(BlueprintCallable, Category = "Animation")
	void SwapWeaponMesh();

	void SwapWeapons(AWeaponBase * WeaponToEquip);

	void ToggleCrouch();

	UFUNCTION(BlueprintCallable, Category = "Movement")
		bool GetIsCrouching() const;

	/** Base turn rate, in deg/sec. Other scaling may affect final turn rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseTurnRate;

	/** Base look up/down rate, in deg/sec. Other scaling may affect final rate. */
	UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Camera")
		float BaseLookUpRate;

	/** Called for forwards/backward input */
	void MoveForward(float Value);

	/** Called for side to side input */
	void MoveRight(float Value);

	void TurnAtRate(float Rate);

	void LookUpRate(float Rate);

	void StartSprint();

	void EndSprint();

	void SetSprint(bool NewSprintState);


	void SetPlayersSpeed(bool NewSprintState);

	bool CheckIfCanSprint();

	void Crouching();

	void UnCrouching();

	void OnJump();

	void EndJump();

	void SetIsJumping(bool newJumpState);

	UFUNCTION(BlueprintCallable, Category = "Movement")
	bool GetIsJumping() const;

	UFUNCTION(BlueprintCallable, Category = "Movement")
	bool GetIsSprinting() const;


private:



	float JumpHeight = 300.f;

	bool bIsJumping = false;

	bool bIsCrouching = false;

	bool bIsDead = false;

	bool bIsSprinting;

	UPROPERTY(BlueprintReadWrite, meta = (AllowPrivateAccess = "true"), Category = "Movement")
		float WalkSpeed = 400;
	UPROPERTY(BlueprintReadWrite, meta = (AllowPrivateAccess = "true"), Category = "Movement ")
		float SprintSpeed = 700;

	/*Weapon*/
public:
	
	UFUNCTION(BlueprintCallable, Category = "Weapon")
	void AddToInventory(class AWeaponBase* NewWeapon);
	void AddAmmo(int32 AmmoAmount, EAmmoType AmmoType);
	void EquipWeapon(AWeaponBase * WeaponToEquip);

	void StartFire();

	void StopFire();

	void Reload();

	class AWeaponBase* Weapon;

	void SwitchToAssaultRifle();

	void SwitchToLaserLaser();

	void SwitchToPistol();

	//UPROPERTY(VisibleAnywhere, BlueprintReadOnly, Category = "Setup")
	

	UFUNCTION(BlueprintCallable, Category = "Aiming")
		bool GetIsAiming() const;

	UFUNCTION(BlueprintCallable, Category = "Setup")
		bool GetIsFiring() const;

private:

	bool bIsAiming = false;

	class AInteractableActor* FocusedActor;
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		float InteractionDistance;
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		bool bEquipNewWeapon = true;
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		FName WeaponSocketName;
	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		FName SecondWeaponSocket;
	bool bIsFiring;

	//Struct Iventory
	UPROPERTY(BlueprintReadWrite, meta = (AllowPrivateAccess = "true"), Category = Hack)
		FPlayerInventory Inventory;

	UPROPERTY(EditDefaultsOnly)
	FName HeadSocketName;
	
	FCollisionQueryParams TraceParams;

protected:

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
	TSubclassOf<AWeaponBase> StartingWeaponBlueprint;

	void CameraZoomIn();

	void CameraZoomOut();

	UPROPERTY(VisibleAnywhere, Category = "Camera")
		float CameraZoomLength;

	float CamCrouchHeight;

	FVector StartingCameraPosition;



};
